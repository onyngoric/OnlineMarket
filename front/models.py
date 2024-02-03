from django.db import models

# Create your models here.
class Ad(models.Model):
    title=models.CharField(max_length=200)
    CATEGORY_OPTIONS=[
        ("3D Printing & Robotics",(("3D Printing Technology","3D Printing Technology"),("Roboticts","Robotics"),)),
        ("Automobile & Vehicles",(('ATVs & Snowmobiles','ATVs & Snowmobiles'),('Bikes, Boats & Watercraft','Bikes, Boats & Watercraft'),('Cars & Heavy Trucks','Cars & Heavy Trucks'),('Damaged & Accident Vehicles','Damaged & Accident Vehicles'),('Automobile Dealers','Automobile Dealers'),('Driving Schools','Driving Schools'),('Parts, Tires & Accessories','Parts, Tires & Accessories'),('Rentals, Lease & Financing','Rentals, Lease & Financing'),('RoadSide Assistance','RoadSide Assistance'))),
        ("Air Transport",(('Aircrafts & Airplanes','Aircrafts & Airplanes'),('Aircraft Dealers','Aircraft Dealers'),('Flight Schools','Flight Schools'),('Parts, Tires, & Accessories','Parts, Tires, & Accessories'),('Rentals, Lease & Financing','Rentals, Lease & Financing'))),
        ("Business",(('Renting','Renting'),('Opportunities','Opportunities'),('Cryptocurrencies','Cryptocurrencies'),('Finance & Investments','Finance & Investments'),('Franchise/ Trading','Franchise/ Trading'),('Partnership & Joint Ventures','Partnership & Joint Ventures'))),
        ("Classes",(('Art, Music & Dance Classes','Art, Music & Dance Classes'),('Computer - Multimedia Classes','Computer - Multimedia Classes'),('Continuing Education','Continuing Education'),('Language Classes','Language Classes'),('Online Bootcamps & Mastermind','Online Bootcamps & Mastermind'),('Sports & Wellness Classes','Sports & Wellness Classes'),('Tutoring - Private Lessons','Tutoring - Private Lessons'))),
        ("Clothing",(('Baby Fashions','Baby Fashions'),('Men Fashions','Men Fashions'),('Women Fashions','Women Fashions'))),
        ("Community",(('Artists, Musicians & Bands','Artists, Musicians & Bands'),('Auctions / Groups','Auctions / Groups'),('Carpool & Rideshare','Carpool & Rideshare'),('Charity, Donate','Charity, Donate'),('Community Activities','Community Activities'),('Elderly Home Assistance','Elderly Home Assistance'),('Household Help','Household Help'),('Lost & Found','Lost & Found'),('Public Announcements','Public Announcements'),('Recreation','Recreation'))),
        ("Construction & Farming Equipments",(('Attachments','Attachments'),('Building Supplies','Building Supplies'),('Construction Equipment','Construction Equipment'),('Damaged & Accident Vehicles','Damaged & Accident Vehicles'),('Farming Equipment','Farming Equipment'),('Rentals, Lease & Financing','Rentals, Lease & Financing'),('RoadSide Assistance','RoadSide Assistance'),('Trailer','Trailer'),('Trucks','Trucks'))),
        ("Electronics",(('Alarms & Security Systems','Alarms & Security Systems'),('Cameras, Camcorders & Drones','Cameras, Camcorders & Drones'),('Computer & Gaming','Computer & Gaming'),('Media & Streaming Equipment','Media & Streaming Equipment'),('Projectors, Tablets & TV','Projectors, Tablets & TV'))),
        ("Freelancing",(('Content Creation','Content Creation'),('Design & Graphics','Design & Graphics'),('Digital Marketing','Digital Marketing'),('Programming & APP Development','Programming & APP Development'),('Social Media Manager','Social Media Manager'),('Video & Animation','Video & Animation'))),
        ("Furniture",(('Beds & Mattresses','Beds & Mattresses'),('Couches & Futons','Couches & Futons'),('Dressers & Wardrobes','Dressers & Wardrobes'),('Office Furniture','Office Furniture'),('Sofas, Chairs & Loveseats','Sofas, Chairs & Loveseats'),('Tables, Recliners & Mirrors','Tables, Recliners & Mirrors'))),
        ("Insurance",(('Auto Insurance & Financing','Auto Insurance & Financing'),('Home Insurance','Home Insurance'),('Insurance Brokers / Agents','Insurance Brokers / Agents'),('Life Insurance','Life Insurance'))),
        ("Jobs",(('Accounting & Finance','Accounting & Finance'),('Administrative & Clerical','Administrative & Clerical'),('Agriculture & Farming','Agriculture & Farming'),('Architect & Design','Architect & Design'),('Arts & Entertainment Jobs','Arts & Entertainment Jobs'),('Babysitter & Nanny','Babysitter & Nanny'),('Bar/Hotel/Guesthouse','Bar/Hotel/Guesthouse'),('Biotech, Science & Pharmacy','Biotech, Science & Pharmacy'),('Civil Services & Policy','Civil Services & Policy'),('Construction & Trades','Construction & Trades'),('Customer Service & Call Centre','Customer Service & Call Centre'),('Domestic Help','Domestic Help'),('Driver & Security','Driver & Security'),('Education / Training & Childcare','Education / Training & Childcare'),('Entry level','Entry level'),('General Labor','General Labor'),('Government & Public Service','Government & Public Service'),('Health Jobs','Health Jobs'),('Health & Wellness Jobs','Health & Wellness Jobs'),('Hospitality, Tourism & Travel','Hospitality, Tourism & Travel'),('Human Resource','Human Resource'),('Import & Export Jobs','Import & Export Jobs'),('Installation, Maintenance & Repair','Installation, Maintenance & Repair'),('Insurance','Insurance'),('Internet','Internet'),('IT & Engineering','IT & Engineering'),('Journalism & Media','Journalism & Media'),('Legal - Paralegal','Legal - Paralegal'),('Management & Executive','Management & Executive'),('Manufacturing & Production','Manufacturing & Production'),('Military','Military'),('Real Estate','Real Estate'),('Research & Development','Research & Development'),('Restaurants','Restaurants'),('Retail & Wholesale','Retail & Wholesale'),('Sales','Sales'),('Shipping & Distribution','Shipping & Distribution'),('Social Work & Nonprofit','Social Work & Nonprofit'),('Teaching','Teaching'),('Transportation & Logistics','Transportation & Logistics'),('Warehouse/Storage','Warehouse/Storage'),('Work From Home','Work From Home'))),
        ("Matrimonial",(('Bride Wear','Bride Wear'),('Groom Wear','Groom Wear'),('Services','Services'),('Wedding Products, Accessories','Wedding Products, Accessories'))),
        ("Pets",(('Equipment & Accessories','Equipment & Accessories'),('Missing Pets','Missing Pets'),('Pets for sale','Pets for sale'))),
        ("Real Estate, Housing & Rentals",(('Agencies / Brokers & Builders','Agencies / Brokers & Builders'),('Apartments For Rent & Lease','Apartments For Rent & Lease'),('Apartments For Sale','Apartments For Sale'),('Cottages For Sale','Cottages For Sale'),('Duplex & Triplex For Sale','Duplex & Triplex For Sale'),('Farmland For Sale','Farmland For Sale'),('Foreclosure Listings','Foreclosure Listings'),('Homes For Sale','Homes For Sale'),('Investment Properties','Investment Properties'),('Lands & Plots For Sale','Lands & Plots For Sale'),('Mobile Homes For Sale','Mobile Homes For Sale'),('Multiplex & Quadruplex For Sale','Multiplex & Quadruplex For Sale'),('New Property Developments','New Property Developments'),('Open House Listings','Open House Listings'),('Parking Spot for Rent','Parking Spot for Rent'),('Real Estate Agents','Real Estate Agents'),('Residential Property Listing','Residential Property Listing'),('Rooms for Rent / Sublet','Rooms for Rent / Sublet'),('Shops For Rent / Lease','Shops For Rent / Lease'),('Vacation Rentals','Vacation Rentals'))),
        ("Sales",(('Clearance & Discount Sale','Clearance & Discount Sale'),('Garage & Moving Sale','Garage & Moving Sale'))),
        ("Services",(('Architects & Interior Designers','Architects & Interior Designers'),('Astrology, Numerology & Vastu','Astrology, Numerology & Vastu'),('Child Care','Child Care'),('Cleaning / Maids','Cleaning / Maids'),('Computer & Consulting','Computer & Consulting'),('Courier Service & Cargo','Courier Service & Cargo'),('Electrician / Handyman','Electrician / Handyman'),('Event Services','Event Services'),('General Contractors','General Contractors'),('Gifts, Flower Delivery & Cakes','Gifts, Flower Delivery & Cakes'),('Handyman','Handyman'),('Health, Beauty & Fitness','Health, Beauty & Fitness'),('Home Mortgage & Improvements','Home Mortgage & Improvements'),('House Keeping / Landscaping','House Keeping / Landscaping'),('Language Translation','Language Translation'),('Lawyers, Advocates & Legal','Lawyers, Advocates & Legal'),('Limousine','Limousine'),('Moving & Storage Services','Moving & Storage Services'),('Music','Music'),('Packers & Movers','Packers & Movers'),('Pest Control','Pest Control'),('Photography & Videography','Photography & Videography'),('Plumbing','Plumbing'),('Recycling','Recycling'),('Restaurants & Food Joints','Restaurants & Food Joints'),('Roofing / Repair','Roofing / Repair'),('Scrap & Junk Removal','Scrap & Junk Removal'),('Tax','Tax'),('Web & Graphic Design','Web & Graphic Design'))),
        ("Softwares",(('Windows','Windows'),('Mac','Mac'),('Open Source','Open Source'))),
        ("Space & Astronomy",(('Equipments','Equipments'),('Jobs','Jobs'),('Missions','Missions'),('Spacecraft','Spacecraft'))),
        ("Tickets",(('Cinema / Theatre / Ballet','Cinema / Theatre / Ballet'),('Discounts / Coupons','Discounts / Coupons'),('Sports / Shows / Tickets','Sports / Shows / Tickets'),('Other Tickets','Other Tickets'))),
        ("Travels, Holiday & Leisure",(('Bus & Train Tickets','Bus & Train Tickets'),('Hotels & Resorts','Hotels & Resorts'),('Taxi & Bus Hire','Taxi & Bus Hire'),('Tour Packages','Tour Packages'),('Travel Agents','Travel Agents'))),
        ("Others...","Others..."),
    ]
    category=models.CharField(max_length=50,choices=CATEGORY_OPTIONS)
    CONDITION_OPTIONS =[
        ("New","New"),
        ("Used-New","Used-New"),
        ("Used-Good","Used-Good"),
        ("Used-Fair","Used-Fair"),
    ]
    condition=models.CharField(max_length=50,choices=CONDITION_OPTIONS,null=True)
    description=models.TextField(max_length=1000)
    DELIVERY_OPTIONS=[
        ("willing to drop off","willing to drop off"),
        ("willing to ship Item","willing to ship Item"),
    ]
    delivery=models.CharField(max_length=50,choices=DELIVERY_OPTIONS,null=True)    
    LOCATION_OPTIONS = [
        ('Alberta','Alberta'),
        ('British Columbia','British Columbia'),
        ('Manitoba','Manitoba'),
        ('New Brunswick','New Brunswick'),
        ('Newfoundland & Labrador','Newfoundland & Labrador'),
        ('NorthWest Territories','NorthWest Territories'),
        ('Nova Scotia','Nova Scotia'),
        ('Nuna Vut','Nuna Vut'),
        ('Ontario','Ontario'),
        ('Prince Edward Island','Prince Edward Island'),
        ('Quebec','Quebec'),
        ('Saskatchewan','Saskatchewan'),
        ('Tukon Territory','Tukon Territory'),
    ]
    location=models.CharField(max_length=50,choices=LOCATION_OPTIONS)
    price=models.IntegerField(null=True)
    PAYMENT_OPTIONS=[
        ("cash","cash"),
        ("E-Transfer","E-Transfer"),
        ("Cash & E-Transfer","Cash & E-Transfer"),
    ]
    payment=models.CharField(max_length=50,choices=PAYMENT_OPTIONS,null=True)
    email=models.EmailField(max_length=200,null=True)
    created_at = models.DateTimeField(auto_now_add=True,null=True)
    
    class Meta:
        verbose_name_plural = "Ads"

class AdImages(models.Model):
    ad = models.ForeignKey(Ad, on_delete=models.CASCADE)
    media=models.FileField(upload_to='images/')
    
    class Meta:
        verbose_name_plural = "AdImages"

class AdMessage(models.Model):
    adId=models.CharField(max_length=200000000000000000000000000)
    poster=models.CharField(max_length=50)
    message=models.CharField(max_length=500)
    created_at = models.DateTimeField(auto_now_add=True,null=True)
    
    class Meta:
        verbose_name_plural = "AdMessages"