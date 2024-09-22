import pandas as pd

# Data for Netflix category codes
data = {
    "Category": [
        "Action & Adventure", "Action Comedies", "Action Sci-Fi & Fantasy", "Action Thrillers", "Adult Animation",
        "Adventures", "African Movies", "Alien Sci-Fi", "Animal Tales", "Anime", "Anime Action", "Anime Comedies",
        "Anime Dramas", "Anime Fantasy", "Anime Features", "Anime Horror", "Anime Sci-Fi", "Anime Series",
        "Art House Movies", "Asian Action Movies", "Australian Movies", "B-Horror Movies", "Baseball Movies",
        "Basketball Movies", "Belgian Movies", "Biographical Documentaries", "Biographical Dramas", "Boxing Movies",
        "British Movies", "British TV Shows", "Campy Movies", "Children & Family Movies", "Chinese Movies",
        "Classic Action & Adventure", "Classic Comedies", "Classic Dramas", "Classic Foreign Movies", "Classic Movies",
        "Classic Musicals", "Classic Romantic Movies", "Classic Sci-Fi & Fantasy", "Classic Thrillers", "Classic TV Shows",
        "Classic War Movies", "Classic Westerns", "Comedies", "Comic Book and Superhero Movies", "Country & Western/Folk",
        "Courtroom Dramas", "Creature Features", "Crime Action & Adventure", "Crime Documentaries", "Crime Dramas",
        "Crime Thrillers", "Crime TV Shows", "Cult Comedies", "Cult Horror Movies", "Cult Movies", "Cult Sci-Fi & Fantasy",
        "Cult TV Shows", "Dark Comedies", "Deep Sea Horror Movies", "Disney", "Disney Musicals", "Documentaries", "Dramas",
        "Dramas based on Books", "Dramas based on real life", "Dutch Movies", "Eastern European Movies", "Education for Kids",
        "Epics", "Experimental Movies", "Faith & Spirituality", "Faith & Spirituality Movies", "Family Features",
        "Fantasy Movies", "Film Noir", "Food & Travel TV", "Football Movies", "Foreign Action & Adventure",
        "Foreign Comedies", "Foreign Documentaries", "Foreign Dramas", "Foreign Gay & Lesbian Movies",
        "Foreign Horror Movies", "Foreign Movies", "Foreign Sci-Fi & Fantasy", "Foreign Thrillers", "French Movies",
        "Gangster Movies", "Gay & Lesbian Dramas", "German Movies", "Greek Movies", "Historical Documentaries",
        "Horror Comedy", "Horror Movies", "Independent Action & Adventure", "Independent Comedies", "Independent Dramas",
        "Independent Movies", "Independent Thrillers", "Indian Movies", "Irish Movies", "Italian Movies", "Japanese Movies",
        "Jazz & Easy Listening", "Kids Faith & Spirituality", "Kids Music", "Kids’ TV", "Korean Movies", "Korean TV Shows",
        "Late Night Comedies", "Latin American Movies", "Latin Music", "Martial Arts Movies", "Martial Arts, Boxing & Wrestling",
        "Middle Eastern Movies", "Military Action & Adventure", "Military Documentaries", "Military Dramas", "Military TV Shows",
        "Miniseries", "Mockumentaries", "Monster Movies", "Movies based on children’s books", "Movies for ages 0 to 2",
        "Movies for ages 2 to 4", "Movies for ages 5 to 7", "Movies for ages 8 to 10", "Movies for ages 11 to 12",
        "Music & Concert Documentaries", "Music", "Musicals", "Mysteries", "New Zealand Movies", "Period Pieces",
        "Political Comedies", "Political Documentaries", "Political Dramas", "Political Thrillers", "Psychological Thrillers",
        "Quirky Romance", "Reality TV", "Religious Documentaries", "Rock & Pop Concerts", "Romantic Comedies",
        "Romantic Dramas", "Romantic Favorites", "Romantic Foreign Movies", "Romantic Independent Movies", "Romantic Movies",
        "Russian", "Satanic Stories", "Satires", "Scandinavian Movies", "Sci-Fi & Fantasy", "Sci-Fi Adventure",
        "Sci-Fi Dramas", "Sci-Fi Horror Movies", "Sci-Fi Thrillers", "Science & Nature Documentaries", "Science & Nature TV",
        "Screwball Comedies", "Showbiz Dramas", "Showbiz Musicals", "Silent Movies", "Slapstick Comedies",
        "Slasher and Serial Killer Movies", "Soccer Movies", "Social & Cultural Documentaries", "Social Issue Dramas",
        "Southeast Asian Movies", "Spanish Movies", "Spiritual Documentaries", "Sports & Fitness", "Sports Comedies",
        "Sports Documentaries", "Sports Dramas", "Sports Movies", "Spy Action & Adventure", "Spy Thrillers",
        "Stage Musicals", "Stand-up Comedy", "Steamy Romantic Movies", "Steamy Thrillers", "Supernatural Horror Movies",
        "Supernatural Thrillers", "Tearjerkers", "Teen Comedies", "Teen Dramas", "Teen Screams", "Teen TV Shows", "Thrillers",
        "Travel & Adventure Documentaries", "TV Action & Adventure", "TV Cartoons", "TV Comedies", "TV Documentaries",
        "TV Dramas", "TV Horror", "TV Mysteries", "TV Sci-Fi & Fantasy", "TV Shows", "Urban & Dance Concerts",
        "Vampire Horror Movies", "Werewolf Horror Movies", "Westerns", "World Music Concerts", "Zombie Horror Movies"
    ],
    "Code": [
        1365, 43040, 1568, 43048, 11881, 7442, 3761, 3327, 5507, 7424, 2653, 9302, 452, 11146, 3063, 10695, 2729, 6721,
        29764, 77232, 5230, 8195, 12339, 12762, 262, 3652, 3179, 12443, 10757, 52117, 1252, 783, 3960, 46576, 31694,
        29809, 32473, 31574, 32392, 31273, 47147, 46588, 46553, 48744, 47465, 6548, 10118, 1105, 2748, 6895, 9584,
        9875, 6889, 10499, 26146, 9434, 10944, 7627, 4734, 74652, 869, 45028, 67673, 59433, 6839, 5763, 4961, 3653,
        10606, 5254, 10659, 52858, 11079, 26835, 52804, 51056, 9744, 7687, 72436, 12803, 11828, 4426, 5161, 2150,
        8243, 8654, 7462, 6485, 10306, 58807, 31851, 500, 58886, 61115, 5349, 89585, 8711, 11804, 4195, 384, 7077,
        3269, 10463, 58750, 8221, 10398, 10271, 751423, 52843, 27346, 5685, 67879, 1402, 1613, 10741, 8985, 6695,
        5875, 2125, 4006, 11, 25804, 4814, 26, 947, 10056, 6796, 6218, 5455, 561, 6962, 90361, 1701, 13335, 9994,
        63782, 12123, 2700, 7018, 6616, 10504, 5505, 36103, 9833, 10005, 3278, 5475, 1255, 502675, 7153, 9916, 8883,
        11567, 6998, 4922, 9292, 1492, 6926, 3916, 1694, 11014, 2595, 52780, 9702, 5012, 13573, 53310, 10256, 8646,
        12549, 3675, 3947, 9196, 58741, 2760, 9327, 5286, 180, 7243, 4370, 10702, 9147, 55774, 11559, 35800, 972,
        42023, 11140, 6384, 3519, 9299, 52147, 60951, 8933, 1159, 10673, 11177, 10375, 10105, 11714, 83059, 4366,
        1372, 83, 9472, 75804, 75930, 7700, 2856, 75405
    ]
}

# Create DataFrame
df = pd.DataFrame(data)

# Save to CSV
df.to_csv('netflix_category_codes.csv', index=False)
