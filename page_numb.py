def get_last_numb_on_page(soup):
    div_page_numbers = soup.find("div", attrs={"class": "pageNumbers"})
    last_number = div_page_numbers.contents[-2].text
    last_number = last_number.replace('\n', '')

    return last_number
