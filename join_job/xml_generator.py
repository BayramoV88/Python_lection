from user_interface import temperature_view
from user_interface import pressure_view
from user_interface import wind_speed_view

def new_create(data, device = 1):
    t, p, w = data
    t = t * 1.8 + 32
    style = 'style="font-size:30px;"'
    xml = '<html>\n <head></head>\n <body>\n'
    xml += '      <p {}> Temperature: {} f</p>\n'\
        .format(t)
    xml += '      <p {}>Pressuare: {} mmHg</p>\n'\
        .format(p)
    xml += '      <p {}>Wind_speed: {} m/s</p>\n'\
        .format(w)
    xml += '    </body>\n<html>'

    with open('new_data.xml', 'w') as page:
        page.write(xml)

    return data