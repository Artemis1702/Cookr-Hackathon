import requests
from bs4 import BeautifulSoup
import spacy
import warnings
warnings.filterwarnings("ignore", category=DeprecationWarning) 

nlp = spacy.load("en_core_web_sm")

# Scrape for the food item
def scrape_food_info(food_item):
    food_name, food_description, tags = scrape_single_word_food_info(food_item)
    
    if food_name and food_description:
        return food_name, food_description, tags
    # Check for multiple words and scrape them individually
    if " " in food_item:
        tags = set()
        words = food_item.split()
        food_name = ""
        food_description = ""
        
        for i, word in enumerate(words):
            name, description, word_tags = scrape_single_word_food_info(word, use_alt_url=True)
                
            if name and description:
                food_name += name + " "
                food_description += description + "\n"
                tags.update(word_tags)
            else:
                print(f"Failed to retrieve information for the word: {word}.")
                
                # Check if there's another word to try
                if i < len(words) - 1:
                    next_word = words[i + 1]
                    print(f"Trying the next word: {next_word}")
                    name, description, word_tags = scrape_single_word_food_info(next_word, use_alt_url=True)
                    if name and description:
                        food_name += name + " "
                        food_description += description + "\n"
                        tags.update(word_tags)
                    else:
                        print(f"Failed to retrieve information for the word: {next_word}.")
                        return None, None, None
                else:
                    print("No more words available.")
                    return None, None, None
        
        return food_name.strip(), food_description.strip(), list(tags)
    else:  
        return None, None, None


# Scrape for the single words in a food item name
def scrape_single_word_food_info(food_item, use_alt_url=False):
    url = f"https://en.wikipedia.org/wiki/{food_item}"
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, "html.parser")

        infobox = soup.find("table", class_="infobox")
        region_or_state = None
        course = None
        place_of_origin = None

        # Check for infobox
        if infobox:
            rows = infobox.find_all("tr")
            for row in rows:
                cells = row.find_all(["th", "td"])
                if len(cells) == 2:
                    header = cells[0].get_text().strip()
                    value = cells[1].get_text().strip()

                    if header == "Region or state":
                        region_or_state = value
                    elif header == "Course":
                        course = value
                    elif header == "Place of origin":
                        place_of_origin = value

            if not all([region_or_state, course, place_of_origin]):
                if use_alt_url:
                    return None, None, None  
                # Check for alternate url if first url does not yield desired results
                alt_url = f"https://en.wikipedia.org/wiki/{food_item}_(food)"
                alt_response = requests.get(alt_url)
                if alt_response.status_code == 200:
                    alt_soup = BeautifulSoup(alt_response.content, "html.parser")
                    alt_infobox = alt_soup.find("table", class_="infobox")
                    if alt_infobox:
                        if not region_or_state:
                            region_element = alt_soup.find("th", text="Region or state")
                            if region_element:
                                sibling = region_element.find_next_sibling("td")
                                if sibling:
                                    region_or_state = sibling.get_text().strip()
                        if not course:
                            course_element = alt_soup.find("th", text="Course")
                            if course_element:
                                sibling = course_element.find_next_sibling("td")
                                if sibling:
                                    course = sibling.get_text().strip()
                        if not place_of_origin:
                            origin_element = alt_soup.find("th", text="Place of origin")
                            if origin_element:
                                sibling = origin_element.find_next_sibling("td")
                                if sibling:
                                    place_of_origin = sibling.get_text().strip()

                        paragraphs = alt_soup.select(".mw-parser-output > p")
                        if paragraphs:
                            content_before_header = []

                            for paragraph in paragraphs:
                                content_before_header.append(paragraph.get_text())

                            food_description = "\n".join(content_before_header)

                            food_name = alt_soup.title.text.split("-")[0].strip()

                            tags = generate_tags(food_description, region_or_state, course, place_of_origin)

                            return food_name, food_description, tags
                        else:
                            return None, None, None
                    else:
                        return None, None, None
                else:
                    print(f"Failed to retrieve information for the food item: {food_item}")
                    return None, None, None

            paragraphs = soup.select(".mw-parser-output > p")
            if paragraphs:
                content_before_header = []

                for paragraph in paragraphs:
                    content_before_header.append(paragraph.get_text())

                food_description = "\n".join(content_before_header)

                food_name = soup.title.text.split("-")[0].strip()

                tags = generate_tags(food_description, region_or_state, course, place_of_origin)

                return food_name, food_description, tags
            else:
                return None, None, None
        else:
            # Check for alternate url if first url does not yield desired results
            alt_url = f"https://en.wikipedia.org/wiki/{food_item}_(food)"
            alt_response = requests.get(alt_url)
            if alt_response.status_code == 200:
                alt_soup = BeautifulSoup(alt_response.content, "html.parser")
                alt_infobox = alt_soup.find("table", class_="infobox")
                if alt_infobox:
                    if not region_or_state:
                        region_element = alt_soup.find("th", text="Region or state")
                        if region_element:
                            sibling = region_element.find_next_sibling("td")
                            if sibling:
                                region_or_state = sibling.get_text().strip()
                    if not course:
                        course_element = alt_soup.find("th", text="Course")
                        if course_element:
                            sibling = course_element.find_next_sibling("td")
                            if sibling:
                                course = sibling.get_text().strip()
                    if not place_of_origin:
                        origin_element = alt_soup.find("th", text="Place of origin")
                        if origin_element:
                            sibling = origin_element.find_next_sibling("td")
                            if sibling:
                                place_of_origin = sibling.get_text().strip()

                    paragraphs = alt_soup.select(".mw-parser-output > p")
                    if paragraphs:
                        content_before_header = []

                        for paragraph in paragraphs:
                            content_before_header.append(paragraph.get_text())

                        food_description = "\n".join(content_before_header)

                        food_name = alt_soup.title.text.split("-")[0].strip()

                        tags = generate_tags(food_description, region_or_state, course, place_of_origin)

                        return food_name, food_description, tags
                    else:
                        return None, None, None
                else:
                    return None, None, None
            else:
                print(f"Failed to retrieve information for the food item: {food_item}")
                return None, None, None
    else:
        print(f"Failed to retrieve information for the food item: {food_item}")
        return None, None, None


# A basic NLP model to find countries and Positive adjectives from food description and generate tags
def generate_tags(food_description, region_or_state=None, course=None, place_of_origin=None):
    tags = set()  
    doc = nlp(food_description)
    
    if region_or_state:
        tags.add(region_or_state.replace("-", " "))
    if course:
        tags.add(course.replace("-", " "))
    if place_of_origin:
        tags.add(place_of_origin.replace("-", " "))
    
    combined_tags = {"Sri Lanka"}  
    for ent in doc.ents:
        if ent.text in combined_tags:
            tags.add(ent.text)
        elif ent.label_ == "GPE":
            tags.add(ent.text)
    for token in doc:
        if token.pos_ == "ADJ" and token.dep_ != "amod" and token.head.pos_ != "NOUN":
            tags.add(token.text.lower())
        elif token.text.lower() == "popular":  
            tags.add(token.text.lower())
    
    if "-" in tags and len(tags) == 1:
        tags.remove("-")
    
    tags.discard("-")
    
    tags = list(set(tags))
    
    return tags  




# food_item = "idli"
# food_name, food_description, tags = scrape_food_info(food_item)

# if food_name and food_description:
#     print(f"Food Item: {food_name}")
#     # print(f"Description: {food_description}")
#     print(f"Tags: {tags}")
# else:
#     print("Failed to retrieve information for the food item.")
