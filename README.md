# UniversalCrawler


CONCEPT:  The basic idea is that I have a made a separate configuration file which holds the nested information about the website to be scrapped. So if you need more features just ad it to the config file.

config-file-details:
    1. class_name is the common name of the class to look 
    2. child tage shows the child node of this node to be crwaled
    3. In case class_name is None, we defind a tag and conduct our search using it
    4. If it a leaf node we stop our search
    5. It a valid python dict so you can have list and any number of nesting you like


I have demonstrated that with two basic feature image and price but it can be easily extended for more.


CODE: The code has a get_data function which is recursive in nature and recursively extracts data using the structure given.