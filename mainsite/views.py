from django.shortcuts import render
from django.http import HttpResponse
from mainsite.models import all_pincodes, country_content
import json ,os
from os.path import exists
# Create your views here.



# Getting Contents For Each Country
def get_content_of_country(country_code, Place_Name, Place_With_Pincode):
    content = country_content.objects.filter(Country_Code = country_code)
    print("======>",len(content))
    if len(content) >0:
        content_of_country = content[0]
        content_of_country = content_of_country.Long_Content
        content_of_country = content_of_country.replace("##Place_Name##",Place_Name)
        content_of_country = content_of_country.replace("##Place_With_Pincode##",Place_With_Pincode)
        content_of_country = content_of_country.replace(", BLANK_DATA","")
        return content_of_country
    else:
        return ""


def load_countries_json():
    countries_json_path = os. getcwd() +'/mainsite/countries.json'
    countries_json = open(countries_json_path)
    countries = json.load(countries_json)
    return countries
def index(request):
    # page_details=all_pincodes.objects.filter(Postal_Code="755012")
    return render(request,'index.html')

def list_of_region(request,country_name):
    countries_json =load_countries_json()
    found_country = {}
    country_name = country_name.replace("+", " ")
    country_name =country_name.upper()
    for i in range(len(countries_json)):
        if country_name.lower() == (countries_json[i]['code']).lower() :
            found_country = countries_json[i]
    res = all_pincodes.objects.order_by().values('State_Name').distinct().filter(Country_Code = found_country['code'])
    resp=[]
    for i in range(len(res)):
        tempdict = {}
        tempdict["content"] = res[i]['State_Name']
        tempdict["country_code"] = country_name
        tempdict["url"] = res[i]['State_Name'].replace(" ", "+")
        resp.append(tempdict)
    
    content_of_country = get_content_of_country(country_name, found_country["name"] ,found_country["name"])
     



    if len(resp) ==1 and resp[0]["content"] == "BLANK_DATA":
        resp=[]
        res = all_pincodes.objects.filter(Country_Code = country_name)
        for i in range(len(res)):
            tempdict = {}
            tempdict["Place_Name"] = res[i].Place_Name
            tempdict["Postal_Code"] = res[i].Postal_Code
            tempdict["url"] = country_name.replace(" ", "+")+"/"+res[i].State_Name.replace(" ", "+")+ "/"+res[i].District_Name_or_City_Name.replace(" ", "+")+ "/"+res[i].Place_Name.replace(" ", "+")+"/pincode-or-zipcode"
            resp.append(tempdict)
        return_res={"pincodes":resp,"county":country_name, "bardcom_name":found_country['name']}
        return render(request,"all_pincodes.html",return_res)

       

    return_res={"contents":resp,"county":country_name, "bardcom_name":found_country['name'], "seo_content":content_of_country}
    return render(request,"region.html",return_res)


def list_of_region_state(request,country_name, state_name):
    countries_json =load_countries_json()
    state_name = state_name.replace("+", " ")
    found_country = {}
    country_name =country_name.upper()
    for i in range(len(countries_json)):
       if country_name.lower() == (countries_json[i]['code']).lower() :
            found_country = countries_json[i]

    res = all_pincodes.objects.order_by().values('District_Name_or_City_Name').distinct().filter(Country_Code = country_name,State_Name = state_name)
    resp=[]

    for i in range(len(res)):
        tempdict = {}
        tempdict["content"] = res[i]['District_Name_or_City_Name']
        tempdict["country_code"] = country_name
        tempdict["url"] = state_name.replace(" ", "+")+ "/"+ res[i]['District_Name_or_City_Name'].replace(" ", "+")
        resp.append(tempdict)
    
    content_of_country = get_content_of_country(country_name, state_name ,state_name)
     

    if len(resp) ==1 and resp[0]["content"] == "BLANK_DATA":
        resp=[]
        res = all_pincodes.objects.filter(Country_Code = country_name)
        for i in range(len(res)):
            tempdict = {}
            tempdict["Place_Name"] = res[i].Place_Name
            tempdict["Postal_Code"] = res[i].Postal_Code
            tempdict["url"] = country_name.replace(" ", "+")+"/"+res[i].State_Name.replace(" ", "+")+ "/"+res[i].District_Name_or_City_Name.replace(" ", "+")+ "/"+res[i].Place_Name.replace(" ", "+")+"/pincode-or-zipcode"
            resp.append(tempdict)
        return_res={"pincodes":resp,"county":country_name, "bardcom_name":state_name}
        return render(request,"all_pincodes.html",return_res)


    return_res={"contents":resp,"county":country_name, "bardcom_name":state_name,"seo_content":content_of_country}
    return render(request,"region.html",return_res)

def list_of_region_state_dict(request,country_name, state_name, dict_name):
    countries_json =load_countries_json()
    state_name = state_name.replace("+", " ")
    dict_name = dict_name.replace("+", " ")
    found_country = {}
    for i in range(len(countries_json)):
       if country_name.lower() == (countries_json[i]['code']).lower() :
            found_country = countries_json[i]
    

    res = all_pincodes.objects.filter(Country_Code = country_name,State_Name = state_name, District_Name_or_City_Name = dict_name)
    resp=[]
    content_of_country = get_content_of_country(country_name, dict_name ,dict_name)
    for i in range(len(res)):
        tempdict = {}
        tempdict["Place_Name"] = res[i].Place_Name
        tempdict["Postal_Code"] = res[i].Postal_Code
        tempdict["url"] = country_name.replace(" ", "+")+"/"+state_name.replace(" ", "+")+ "/"+res[i].District_Name_or_City_Name.replace(" ", "+")+ "/"+res[i].Place_Name.replace(" ", "+")+"/pincode-or-zipcode"
        resp.append(tempdict)
    return_res={"pincodes":resp,"county":country_name, "bardcom_name":dict_name, "seo_content":content_of_country}
    return render(request,"all_pincodes.html",return_res)

def list_of_region_state_dict_pin_det(request,country_name, state_name, dict_name,place_name):
    countries_json =load_countries_json()
    state_name = state_name.replace("+", " ")
    dict_name = dict_name.replace("+", " ")
    place_name = place_name.replace("+", " ")
    found_country = {}
    for i in range(len(countries_json)):
        if country_name == countries_json[i]['code']:
            found_country = countries_json[i]
    
    resp = all_pincodes.objects.filter(Country_Code = country_name,State_Name = state_name, District_Name_or_City_Name = dict_name, Place_Name = place_name)

    content_of_country = get_content_of_country(country_name, place_name ,place_name+", "+dict_name+", "+state_name +" is "+resp[0].Postal_Code)

    return_res={"pincode_details":resp,"county":country_name,"found_country":found_country , "bardcom_name": place_name, "seo_content":content_of_country}
    return render(request,"pincode_details.html",return_res)

def search_pincode(request,pincode):
    res = all_pincodes.objects.filter(Postal_Code = pincode)
    resp=[]
    if (len(res) > 0):
        for i in range(len(res)):
            tempdict = {}
            tempdict["Place_Name"] = res[i].Place_Name
            tempdict["Postal_Code"] = res[i].Postal_Code
            tempdict["url"] = res[i].Country_Code.replace(" ", "+")+"/"+res[i].State_Name.replace(" ", "+")+ "/"+res[i].District_Name_or_City_Name.replace(" ", "+")+ "/"+res[i].Place_Name.replace(" ", "+")+"/pincode-or-zipcode"
            resp.append(tempdict)
        return_res={"pincodes":resp,"county":res[i].Country_Code, "bardcom_name" : res[i].State_Name}
        return render(request,"all_pincodes.html",return_res)
    else:
        res = {"errormessage": "Pincode Not Found. Search A Valid Pincode."}
        return render(request,"return.html",res)

def sitemap22(request):
    res = all_pincodes.objects.order_by().values('Country_Code').distinct()

    print(len(res),res[0]["Country_Code"])
    countrylist =[]
    for i in range(len(res)):
       countrylist.append(res[i]["Country_Code"])
    counter =0 
    limit=30000
    filecounter= 1
    fistline =0
    file_name = "static/sitemap/sitemap"+str(filecounter)+".xml"
    top = '''<?xml version="1.0" encoding="UTF-8"?>
            <sitemapindex xmlns="http://www.sitemaps.org/schemas/sitemap/0.9"><sitemap>
            '''
    deup={}

    for i in (countrylist):
        rest = all_pincodes.objects.filter(Country_Code=i)
        for j in range(len(rest)):
            url = "https://globalpincode.org/region/"+i+"/"+rest[j].State_Name.replace(" ", "+")+"/"+rest[j].District_Name_or_City_Name.replace(" ", "+")+"/"+rest[j].Place_Name.replace(" ", "+")+"/pincode-or-zipcode"
            
            if url not in deup:
                deup[url] =""

                text ='''<sitemap>
                            <loc>'''+url+'''</loc>
                            <lastmod>2023-02-14T06:18:47+00:00</lastmod>
                        </sitemap>'''
                if int(counter/limit) != 1:
                    f = open(file_name, "a")
                    if fistline ==0:
                        text = top +text
                        fistline= 1
                    f.write(text)
                    f.close()
                    counter= counter+1
                else:
                    f = open(file_name, "a")
                    end="</sitemapindex>"
                    f.write(end)
                    f.close()
                    filecounter = filecounter+1
                    file_name = "static/sitemap/sitemap"+str(filecounter)+".xml"
                    counter = 0 
                    fistline =0
            
def sitemap1(request):
    top = '''<?xml version="1.0" encoding="UTF-8"?><?xml-stylesheet type="text/xsl" href="//globalpincode.org/main-sitemap.xsl"?>
        <sitemapindex xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">'''
    text = top
    
    for i in range(1,53):
        url = "https://globalpincode.org/static/sitemap/sitemap"+str(i)+".xml"
        text1 ='''<sitemap>
                        <loc>'''+url+'''</loc>
                        <lastmod>2023-02-14T06:18:47+00:00</lastmod>
                    </sitemap>'''
        
        text = text+text1
    text = text+ "</sitemapindex>"
    return HttpResponse(text)
    
# with open(r"/Users/bibekanandabhuyan/Projects/find_code/find_code/sitemap51.xml", 'r') as fp:
#     lines = len(fp.readlines())
#     print('Total Number of lines:', lines)