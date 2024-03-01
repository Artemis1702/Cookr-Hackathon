# Cookr-Hackathon 2024
This repository contains my code for Cookr Hackathon 2024. 
## Question 1 - Item Categorization. 40 marks
Create a model or research the necessary steps to create a model for categorizing items. When the cook adds an item to their kitchen, it should be automatically categorized into multiple categories. 
### Problems faced 
* Understanding the problem statement
* Finding suitable websites and apis related to food and cuisines
* Using Natural Language Processing (NLP) to generate tags
### My Approach
* I initially started to work on the problem statement by searching for available datasets.
* But then I decided to web scrape for the required Food Item when needed and then use NLP techniques to identify adjectives with positive sentiment and also identify country of origin, course type (breakfast, lunch or dinner) and other relevant information.
* I tried seaarching for various websites with details about food items and dishes and finally settled for wikipedia.
* My algorithm searches for the wikipedia page of the food_item, and scrapes it if available and generates the required tags using NLP.
* If the wikipedia page is nnot available, it tries to split the name of the food item into multiple words and searches for those respective items. Eg: "Ragi Dosa" is split into "Ragi" and "Dosa" and searched separately and the tags are added together and displayed.
* If the dish is not available, it says that "The given food item is not available".
* I then built a simple Tkinter UI to display the output of the algorithm in a way that is easy to understand even for a layman.
### Output
<img width="959" alt="Idli" src="https://github.com/Artemis1702/Cookr-Hackathon/assets/76508539/486df3a4-dbb4-4e3a-9fb1-170de1106324">
<img width="959" alt="Ragi Dosa" src="https://github.com/Artemis1702/Cookr-Hackathon/assets/76508539/7de21f29-c56c-4439-ae30-a14499665fdf">
<img width="959" alt="Chicken Vindaloo" src="https://github.com/Artemis1702/Cookr-Hackathon/assets/76508539/3751c8c3-f508-4b57-916c-10d6e8598681">

### Enhancements and Directions for Further Developmen
* My main Idea was to create something like chatGPT but only for foods. Which would give the tags and other information for the input Food Item.
  * To achieve the above functionality we can increase the number of websites we scrape the information from instead of limiting to only one website (Wikipedia).
  * We can also enhance the NLP model to detect all words related to food industry and then choose the required tags from them.
* The above suggestions could not be implemented by me, due to the limited time constraints.

## Question 2 - Last Mile Delivery Batching. 60 marks
It is crucial in today’s last-mile delivery ecosystem to optimize for speed, and cost efficiencies. Smarter algorithms play a crucial role in the ecommerce marketplace deliveries We need to group/batch the delivery of multiple items to the same rider without losing time. Here are several scenarios where we need smart operational research algorithms.
* Rule # 1
  * Two orders - From the same kitchen.
  * To the same customer.
  * Ready at the same time (10 mins apart).
  * Assign the pick-up to the same rider.
* Rule # 2:
  * Two orders.
  * From two different kitchens (1 km apart).
  * To the same customer.
  * Ready at the same time (10 mins apart).
  * Assign the pick-up to the same rider.
* Rule # 3:
  * Two orders.
  * From the same kitchen.
  * To two different customers (1 km apart).
  * Ready at the same time (10 mins apart).
  * Assign the pick-up to the same rider.
* Rule # 4:
  * Two orders.
  * From two different kitchens (1 km apart).
  * To the same customer.
  * Ready at the same time (10 mins apart).
  * Assign the pick-up to the same rider.
* Rule # 5:
  * Two orders.
  * From two different kitchens (1 km apart).
  * To the same customer.
  * Ready at the same time (10 mins apart).
  * Assign the pick-up to the same rider.
* Rule # 6:
  * Two orders. 
  * To the same customer.
  * 2nd kitchens pick up on the way to the customer.
  * Ready at the time the rider reaches the second kitchen (10 mins apart).
  * Assign the pick-up to the same rider.
* Rule # 7:
  * Two orders.
  * 2nd customers drop on the way to the 1st customer (Vice Versa).
  * 2nd kitchens pick up on the way to the customer.
  * Ready at the same time (10 mins apart or by the time rider reaches the kitchen).
  * Assign the pick-up to the same rider.
* Rule # 8:
  * Two orders.
  * From the same kitchen.
  * 2nd customers drop on the way to the customer 1st (Vice Versa).
  * Ready at the same time (10 mins apart).
  * Assign the pick-up to the same rider.
