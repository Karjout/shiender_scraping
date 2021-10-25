# By Karjout Abdeslam <br/>
# step1 = "install required modules" <br/>
    modules ="requests , json, BeautifulSoup' <br/>
    install Module =" pip3 install <ModuleName>" <br/>
    examples = "pip 3 install json"  <br/>

# step 2 = <br/>
    launch first scrap_items.py  using python scrap_items.py <br/>
    until you get Link.txt <br/>
# step 3 = <br/>
    launch items.py using python items.py <br/>
    until you get ids.txt <br/>
# step 4 =  <br/>
    launch final.py using python final.py <br/>
    you will get the Product.json that contain the format  bellow <br/>
   ``` Product.json format <br/> 
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
```
