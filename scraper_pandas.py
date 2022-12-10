import pandas as pd
import ssl

ssl._create_default__https_context = ssl._create_unverified_context

scraper = pd.read_html("https://en.wikipedia.org/wiki/Comparison_of_Linux_distributions")

for idx, table in enumerate(scraper):
    print("*************************************************************************************************************************")
    print(idx)
    print(table)
