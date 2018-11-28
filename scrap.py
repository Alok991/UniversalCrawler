import requests
from bs4 import BeautifulSoup as soup
from config import structure

WEBSITE = "https://amazon.in"



def get_tag_data(tag, position_in_page):
    if(tag == "img"):
        return get_img_data(position_in_page)
    elif(tag == "span"):
        return get_span_data(position_in_page)


def get_img_data(position_in_page):
    # TODO
    # We still have to do position_in_page.find("img") and then process
    print("TODO img data")
    pass

def get_span_data(position_in_page):
    # TODO
    print("TODO span data")
    pass


def get_data(current_structure, position_in_page):

    # Base case
    if(current_structure["leaf"]):
        # We have a terminal node in our structure tree
        tag = current_structure["tag"]
        data = get_tag_data(tag, position_in_page)
        # TODO: Write data to a file here
    else:
        if(current_structure["class_name"] is None):
            # This is a tag and not a class, nor it is a leaf node
            position_in_page = position_in_page.find(current_structure["tag"])
            for child_i in current_structure["child"]:
                get_data(child_i, position_in_page)
        else:
            # Now this is a class which will have more data
            position_in_page_list = position_in_page.find_all(class_=current_structure["class_name"])
            for position_in_page in position_in_page_list:
                for child_i in current_structure["child"]:
                    get_data(child_i, position_in_page)


        

if __name__ == "__main__":
    page = requests.get(WEBSITE)
    page = soup(page.content, 'html.parser')
    get_data(structure, page)