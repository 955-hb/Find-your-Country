import plotly.express as px


def run_program():
    while True:

        country = input('Enter the country name: ')
        data = {
            'Country': [country],
            'Values': [100]
        }

        fig = px.choropleth(
            data,
            locations='Country',
            locationmode='country names',
            color='Values',
            color_continuous_scale='Inferno',
            title=f'Country Map Highlighting {country}'
        )
        fig.show()

        restart = input('do you want to end the program? (y/n)')

        if restart == 'y':
            print('Application successfully closed.')
            break


run_program()
