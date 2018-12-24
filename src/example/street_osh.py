def extractdata(context, data):
    # This stage comes after 'fetch' so the 'data' input contains an
    # HTTPResponse object.
    response = context.http.rehash(data)
    url = response.url
    page = response.html

    # Parse the rest of the page to extract structured data.
    
    for i in range(1, len(page.xpath('//tbody/tr')) + 1):
        number = (_gettext(page.xpath('//tbody/tr['+str(i)+']/td[1]/text()')))
        id_street = (_gettext(page.xpath('//tbody/tr['+str(i)+']/td[2]/text()')))
        street_kg = (_gettext(page.xpath('//tbody/tr['+str(i)+']/td[3]/div/p/text()')))
        street_ru = (_gettext(page.xpath('//tbody/tr['+str(i)+']/td[4]/div/p/text()')))
        old_kg = (_gettext(page.xpath('//tbody/tr['+str(i)+']/td[5]/div/p/text()')))
        old_ru = (_gettext(page.xpath('//tbody/tr['+str(i)+']/td[6]/div/p/text()')))
        nas_punkt = (_gettext(page.xpath('//tbody/tr['+str(i)+']/td[7]/text()')))
        
        org_data = {
        "number": number,
        "id_street": id_street,
        "street_kg": street_kg,
        "street_ru": street_ru,
        "old_kg": old_kg,
        "old_ru": old_ru,
        "nas_punkt": nas_punkt
        }
        url_dict = {
            'url': get_next_url(url)
            }
        print(url)
        print(get_next_url(url))
        context.emit(rule="store", data=clean_dict(org_data))
        print("----------------PRINTING ORG_DATA----------------")
        print(org_data)
    context.emit(rule="fetch", data=url_dict)
        
def get_next_url(url): 
    spl_1=url.split("page=")
    spl_2=spl_1[1].split("&")
    num = int(spl_2[0])+1
    return spl_1[0]+"page="+str(num)+"&"+spl_2[1]
    
def clean_dict(data):
    result = {}
    for key, value in data.items():
        if value is None or value=='' or value ==[]:
            value = '__'
            result[key] = value
        else:
            result[key] = data[key]
    return result    
    
def _gettext(list):
    if not list:
        return list
    else:
        return list[0].strip()