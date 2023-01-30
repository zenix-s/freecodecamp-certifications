# q: list all fonts in the system that are monospaced
# a: use the font manager to get a list of all fonts
#    and then filter the list for monospaced fonts
#    and print the results

import matplotlib.font_manager as fm

# get a list of all fonts
font_list = fm.findSystemFonts()


# filter the list for monospaced fonts
monospaced = [f for f in font_list if fm.FontProperties(fname=f).get_name() == 'monospace']





# print the results
print('monospaced fonts:')
for f in monospaced:
    print(f)

    

# end of file


    

