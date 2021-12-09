# Roblox-check-items-from-API

An application I wrote for quite awhile ago but thought it was pretty cool so might as well share it. 
It was a request from someone that wanted to calculate the wealth (total item price) for various users that was scraped across different groups on the site. Another one also used it to regularly update the wealthiest users in their clan. Have never played the game myself so I wouldn't know more.

For all usernames in the *users.txt* file it scraps their inventory and iterates over all product prices. 

It values the products based on the current marketprice, so some items might be valued to what their not actually worth (e.g some T-shirts). Then totalValue is appended with the username to *usersPrice.txt.* It also parses if user has offSale items.

There's also another file *rareItems.txt* which can be used if you value certaint items. So if the user has these they will also be noted as the offsale example with an unique line of code.

Thought it could be left Open-source if anyone wants to quickly calculate their own or other players wealth. There is no functionality of that on the Roblox Website.

//
