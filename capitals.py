

countryes_list = input().split(', ')
capitals_list = input().split(', ')

country_capital = {country: capital for country, capital in zip(countryes_list, capitals_list)}

# for country, capital in country_capital.items():
#     print(f'{country} -> {capital}')
#    print(f'{country} -> {country_capital[country]},\n')
print(*[f'{country} -> {capital}' for country, capital in country_capital.items()],sep='\n')