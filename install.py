# Installer for Belchertown weewx skin
# Pat O'Brien, 2018

from setup import ExtensionInstaller

def loader():
    return ExfoliationInstaller()

class ExfoliationInstaller(ExtensionInstaller):
    def __init__(self):
        super(ExfoliationInstaller, self).__init__(
            version="0.8.2",
            name='Belchertown',
            description='A clean modern skin with real time streaming updates and interactive charts. Modeled after BelchertownWeather.com',
            author="Pat OBrien",
            author_email="pat@obrienlabs.net",
            config={
                'StdReport': {
                    'Belchertown': {
                        'skin':'Belchertown',
                        'HTML_ROOT':'belchertown'
                    },
                    'Highcharts_Belchertown': {
                        'skin':'Highcharts_Belchertown',
                        'HTML_ROOT':'belchertown'
                    }
                }
            },
            files=[('bin/user', ['bin/user/belchertown.py',
                                 'bin/user/belchertown_highchartsSearchX.py'
                                ]
                    ),
                   ('skins/Belchertown', ['skins/Belchertown/favicon.ico',
                                          'skins/Belchertown/footer.html.tmpl',
                                          'skins/Belchertown/header.html.tmpl',
                                          'skins/Belchertown/index.html.tmpl',
                                          'skins/Belchertown/about.inc.example',
                                          'skins/Belchertown/index_custom_hooks.inc.example',
                                          'skins/Belchertown/manifest.json.tmpl',
                                          'skins/Belchertown/records.inc.example',
                                          'skins/Belchertown/skin.conf',
                                          'skins/Belchertown/style.css'
                                         ]
                    ),
                   ('skins/Belchertown/about', ['skins/Belchertown/about/index.html.tmpl']),
                   ('skins/Belchertown/graphs', ['skins/Belchertown/graphs/index.html.tmpl']),
                   ('skins/Belchertown/NOAA', ['skins/Belchertown/NOAA/NOAA-YYYY-MM.txt.tmpl',
                                               'skins/Belchertown/NOAA/NOAA-YYYY.txt.tmpl'
                                              ]
                    ),
                   ('skins/Belchertown/pi', ['skins/Belchertown/pi/index.html.tmpl',
                                               'skins/Belchertown/pi/pi-header.html.tmpl'
                                              ]
                    ),                    
                   ('skins/Belchertown/records', ['skins/Belchertown/records/index.html.tmpl']),
                   ('skins/Belchertown/reports', ['skins/Belchertown/reports/index.html.tmpl']),
                   ('skins/Belchertown/js', ['skins/Belchertown/js/highcharts-dayplots.js.tmpl',
                                             'skins/Belchertown/js/highcharts-weekplots.js.tmpl',
                                             'skins/Belchertown/js/highcharts-monthplots.js.tmpl',
                                             'skins/Belchertown/js/highcharts-yearplots.js.tmpl',
                                             'skins/Belchertown/js/index.html',
                                             'skins/Belchertown/js/responsive-menu.js'
                                            ]
                    ),
                   ('skins/Belchertown/json', ['skins/Belchertown/json/index.html',
                                               'skins/Belchertown/json/weewx_data.json.tmpl'
                                              ]
                    ),
                   ('skins/Belchertown/images', ['skins/Belchertown/images/clear-day.png',
                                                 'skins/Belchertown/images/clear-night.png',
                                                 'skins/Belchertown/images/cloudy.png',
                                                 'skins/Belchertown/images/fog.png',
                                                 'skins/Belchertown/images/hail.png',
                                                 'skins/Belchertown/images/partly-cloudy-day.png',
                                                 'skins/Belchertown/images/partly-cloudy-night.png',
                                                 'skins/Belchertown/images/rain.png',
                                                 'skins/Belchertown/images/sleet.png',
                                                 'skins/Belchertown/images/snow.png',
                                                 'skins/Belchertown/images/snowflake-icon-15px.png',
                                                 'skins/Belchertown/images/station.png',
                                                 'skins/Belchertown/images/station48.png',
                                                 'skins/Belchertown/images/station72.png',
                                                 'skins/Belchertown/images/station96.png',
                                                 'skins/Belchertown/images/station144.png',
                                                 'skins/Belchertown/images/station168.png',
                                                 'skins/Belchertown/images/station192.png',
                                                 'skins/Belchertown/images/sunrise.png',
                                                 'skins/Belchertown/images/sunset.png',
                                                 'skins/Belchertown/images/thunderstorm.png',
                                                 'skins/Belchertown/images/tornado.png',
                                                 'skins/Belchertown/images/wind.png',
                                                 'skins/Belchertown/images/index.html'
                                                ]
                    ),
                   ('skins/Highcharts_Belchertown', ['skins/Highcharts_Belchertown/skin.conf']
                    ),
                   ('skins/Highcharts_Belchertown/json', ['skins/Highcharts_Belchertown/json/day.json.tmpl',
                                                          'skins/Highcharts_Belchertown/json/week.json.tmpl',
                                                          'skins/Highcharts_Belchertown/json/month.json.tmpl',
                                                          'skins/Highcharts_Belchertown/json/year.json.tmpl',
                                                         ]
                    )
                   ]
        )
