def extractdata(context, data):
    # This stage comes after 'fetch' so the 'data' input contains an
    # HTTPResponse object.
    response = context.http.rehash(data)
    url = response.url
    page = response.html

    # Parse the rest of the page to extract structured data.


    for i in range(1,len(page.xpath('//tbody/tr'))+1):
        name_city = (_gettext(page.xpath('//tbody/tr['+str(i)+']/td[7]/text()')))
        id_street = (_gettext(page.xpath('//tbody/tr['+str(i)+']/td[2]/text()')))
        street_kg = (_gettext(page.xpath('//tbody/tr['+str(i)+']/td[3]/div/p/text()')))

        org_data = {
        "name_city": name_city,
        "id_street": id_street,
        "street_kg": street_kg,
        }

        context.emit(data=org_data)
        print("------------------------------------ORG_DATA--------------------------------------")
        print(org_data)


def clean_dict(data):
    result = {}
    for key, value in data.items():
        if value is None or value == '' or value == []:
            value = '--'
            result[key] = value
        else:
            result[key] = data[key]
    return result


def _gettext(list):
    if not list:
        return list
    else:
        return list[0].strip()

