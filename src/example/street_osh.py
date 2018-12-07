def extractdata(context, data):
    # This stage comes after 'fetch' so the 'data' input contains an
    # HTTPResponse object.
    response = context.http.rehash(data)
    url = response.url
    page = response.html

    # Parse the rest of the page to extract structured data.

   
    street = _gettext(page.xpath("//tbody/tr['+str(j)+']/td[3]//p/text()"))
   

    org_data = {
        "url": response.url,
		"street": street,
		
    }
    
	
    context.emit(data=org_data)

def _gettext(list):
    if not list:
        return list
    else:
        return list[0].strip()
        
    for i in range(len(rows)):
        j = i+1
        result = {}
        street = _gettext((tree.xpath('//tbody/tr['+str(j)+']/td[3]//p/text()')))
        result[street] = street