from amazon_scrap import Amazon_Scraper

scraper = Amazon_Scraper(keyword="engineering books", num_books=30, slp_time=5)
df = scraper.get_books()
df.to_csv("engineering_books.csv", index=False)