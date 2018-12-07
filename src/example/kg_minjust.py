def extractdata(context, data):
    # This stage comes after 'fetch' so the 'data' input contains an
    # HTTPResponse object.
    response = context.http.rehash(data)
    url = response.url
    page = response.html

    # Parse the rest of the page to extract structured data.

    name_ru = _gettext(page.xpath("//span[contains(text(),'2. П')]/../../following-sibling::td//text()"))
    full_name_kg = _gettext(page.xpath("//span[contains(text(),'1. П')]/../../following-sibling::td//text()"))
    short_name_kg = _gettext(page.xpath("//span[contains(text(),'3. С')]/../../following-sibling::td//text()"))
    short_name_ru = _gettext(page.xpath("//span[contains(text(),'4. С')]/../../following-sibling::td//text()"))
    legal_form = _gettext(page.xpath("//span[contains(text(),'5. О')]/../../following-sibling::td//text()"))
    foreign_participation = _gettext(page.xpath("//span[contains(text(),'6. Е')]/../../following-sibling::td//text()"))
    registration_number = _gettext(page.xpath("//span[contains(text(),'7. Р')]/../../following-sibling::td//text()"))
    okpo = _gettext(page.xpath("//span[contains(text(),'8. Р')]/../../following-sibling::td//text()"))
    inn = _gettext(page.xpath("//span[contains(text(),'9. И')]/../../following-sibling::td//text()"))
    region = _gettext(page.xpath("//span[contains(text(),'10. О')]/../../following-sibling::td//text()"))
    district = _gettext(page.xpath("//span[contains(text(),'11. Р')]/../../following-sibling::td//text()"))
    city  = _gettext(page.xpath("//span[contains(text(),'12. Г')]/../../following-sibling::td//text()"))
    microdistr = _gettext(page.xpath("//span[contains(text(),'13. М')]/../../following-sibling::td//text()"))
    street = _gettext(page.xpath("//span[contains(text(),'14. У')]/../../following-sibling::td//text()"))
    home = _gettext(page.xpath("//span[contains(text(),'15. ')]/../../following-sibling::td//text()"))
    appartment = _gettext(page.xpath("//span[contains(text(),'16. ')]/../../following-sibling::td//text()"))
    phone = _gettext(page.xpath("//span[contains(text(),'17. Т')]/../../following-sibling::td//text()"))
    fax = _gettext(page.xpath("//span[contains(text(),'18. Ф')]/../../following-sibling::td//text()"))
    mail = _gettext(page.xpath("//span[contains(text(),'19. Э')]/../../following-sibling::td//text()"))
    rereg = _gettext(page.xpath("//span[contains(text(),'20. Г')]/../../following-sibling::td//text()"))
    date_Order = _gettext(page.xpath("//span[contains(text(),'21. Д')]/../../following-sibling::td//text()"))
    first_date = _gettext(page.xpath("//span[contains(text(),'22. Д')]/../../following-sibling::td//text()"))
    method_of_creating = _gettext(page.xpath("//span[contains(text(),'23. С')]/../../following-sibling::td//text()"))
    type_of_ownership = _gettext(page.xpath("//span[contains(text(),'24. Ф')]/../../following-sibling::td//text()"))                        
    head_name_sur = _gettext(page.xpath("//span[contains(text(),'25. Ф')]/../../following-sibling::td//text()"))
    main_activity_type = _gettext(page.xpath("//span[contains(text(),'26. О')]/../../following-sibling::td//text()"))
    eco_activity_code = _gettext(page.xpath("//span[contains(text(),'27. К')]/../../following-sibling::td//text()"))
    participants_phys_quan = _gettext(page.xpath("//span[contains(text(),'28. К')]/../../following-sibling::td//text()"))
    participants_jur_quan = _gettext(page.xpath("//span[contains(text(),'29. К')]/../../following-sibling::td//text()"))
    participants_total = _gettext(page.xpath("//span[contains(text(),'30. О')]/../../following-sibling::td//text()"))
    participants = _gettext(page.xpath("//span[contains(text(),'31. У')]/../../following-sibling::td//text()"))
    participant = _gettext(page.xpath("//span[contains(text(),'Учредитель')]/../../following-sibling::td//text()"))

    org_data = {
        "url": response.url,
        "name_ru": name_ru,
		"full_name_kg": full_name_kg,
		"short_name_kg": short_name_kg,
		"short_name_ru": short_name_ru,
		"legal_form": legal_form,
		"foreign_participation": foreign_participation,
		"registration_number": registration_number,
		"okpo": okpo,
		"inn": inn,
		"region": region,
		"district": district,
		"city": city,
		"microdistr": microdistr,
		"street": street,
		"home": home,
		"appartment": appartment,
		"phone": phone,
		"fax": fax,
		"mail": mail,
		"Rereg": rereg,
		"Date_Order": date_Order,
		"First_date": first_date,
		"Method_of_creating": method_of_creating,
		"Type_of_ownership": type_of_ownership,
		"head_name_sur":head_name_sur,
		"main_activity_type": main_activity_type,
		"eco_activity_code": eco_activity_code,
		"participants_phys_quan": participants_phys_quan,
		"participants_jur_quan": participants_jur_quan,
		"participants_total": participants_total,
		"participants": participants,
		"participant": participant
    }
    clean_org_data = clean_dict(org_data)
    context.emit(data=clean_org_data)
    
    print("-------------------------------------org_data-------------------------------------")
    print(org_data)
    
def clean_dict(items):
    result = {}
    for key, value in items.items():
        if value is None or value == '' or value == []:
            value = '---'
            result[key] = value
        else:
            result[key] = items[key]
    return result
    
    
        
    
    
def _gettext(list):
    if not list:
        return list
    else:
        return list[0].strip()