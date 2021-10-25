#By Karjout Abdeslam
 step1 = "install required modules" 
    modules ="requests , json, BeautifulSoup'
    install Module =" pip3 install <ModuleName>"
    examples = "pip 3 install json"  

step 2 = 
    launch first scrap_items.py  using python scrap_items.py
    until you get Link.txt 
step 3 = 
    launch items.py using python items.py
    until you get ids.txt
step 4 = 
    launch final.py using python final.py
    you will get the Product.json that contain the format  bellow
    Product.json format 
        {
            "repositoryId": "66123",
            "commercialReference": "66123",
            "description": "MGE Network Management Card with ModBus/Jbus",
            "price": "null",
            "currency": "null",
            "pictureUrl": "https://download.schneider-electric.com/files?p_Doc_Ref=SPD_STOS-7RT8Q9_FL_H&p_File_Type=rendition_113_png&default_image=DefaultProductImage.png",
            "pictureAltText": "Schneider Electric 66123 Image",
            "pdpUrl": "https://www.se.com/ww/en/product/66123/mge-network-management-card-with-modbus-jbus/"
        }

