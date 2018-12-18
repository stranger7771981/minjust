def extractdata(context, data):
    # This stage comes after 'fetch' so the 'data' input contains an
    # HTTPResponse object.
    response = context.http.rehash(data)
    url = response.url
    page = response.html

    # Parse the rest of the page to extract structured data.

    streets = page.xpath("//td[3]/div[@class='list-street']/p")

    for i in range(len(streets)):
        street = page.xpath('//tbody/tr['+str(i)+']/td[3]//p/text()')
        if (len(street)> 0):
            street_str = street[0]
        else:
            street_str = street
        org_data = {
        "url": response.url,
        "street": street,
        }
    context.emit(data=org_data)


def _gettext(list):
    if not list:
        return list
    else:
        print (list)

