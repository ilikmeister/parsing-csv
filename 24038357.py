def main(csvfile, age_group, country):
    # Opening the file
    file = open(csvfile)
    
    # Skipping the first line of headlines
    next(file)
    
    # Initializing variables
    student_details = []
    unique_countries = set()
    total_time = total_income = count_people = 0
    dataset_income = []
    total_urban = count_urban = total_sub_urban = count_sub_urban = total_rural = count_rural = 0
    count_facebook = count_instagram = count_youtube = 0
    dataset_income_facebook = []
    dataset_age_facebook = []
    dataset_income_instagram = []
    dataset_age_instagram = []
    dataset_income_youtube = []
    dataset_age_youtube = []
    total_age_facebook = total_age_youtube = total_age_instagram = total_income_facebook = total_income_youtube = total_income_instagram = numerator = 0
    dataset_age_highest_platform = []
    dataset_income_highest_platform = []
    avg_age_highest_platform = avg_income_highest_platform = count_highest_platform = 0
    
    # Loop through the file's each line
    for line in file:
        # Extracting the data
        user_id, age, gender, time_spent_hour, platform, interests, country_fromcsv, demographics, profession, income, indebt = line.strip().split(',')
        
        # Checking for the matching criteria for the first output and adding to the student_details list
        if country_fromcsv.lower() == country.lower() and indebt == 'TRUE' and int(time_spent_hour) > 7:
            student_details.append([user_id, int(income)])
        
        # Checking for the age_group for the second and third outputs   
        if int(age) in range(age_group[0], age_group[1] + 1):
            # Adding unique countries to the list
            unique_countries.add(country_fromcsv.lower())
            
            # Calculations for the third output
            total_time = total_time + int(time_spent_hour)
            total_income = total_income + int(income)
            count_people = count_people + 1
            dataset_income.append(int(income))
            
            # Checking for the demographics, summing the time spent and number of people           
            if demographics.lower() == 'urban':
                total_urban = total_urban + int(time_spent_hour)
                count_urban = count_urban + 1
            elif demographics.lower() == 'sub_urban':
                total_sub_urban = total_sub_urban + int(time_spent_hour)
                count_sub_urban = count_sub_urban + 1
            elif demographics.lower() == 'rural':
                total_rural = total_rural + int(time_spent_hour)
                count_rural = count_rural + 1
        
        # Checking for the platform type, summing several statistics and adding items to the lists      
        if platform.lower() == 'facebook':
            count_facebook = count_facebook + 1
            total_income_facebook = total_income_facebook + int(income)
            total_age_facebook = total_age_facebook + int(age)
            dataset_income_facebook.append(int(income))
            dataset_age_facebook.append(int(age))
        elif platform.lower() == 'instagram':
            count_instagram = count_instagram + 1
            total_income_instagram = total_income_instagram + int(income)
            total_age_instagram = total_age_instagram + int(age)
            dataset_income_instagram.append(int(income))
            dataset_age_instagram.append(int(age))
        elif platform.lower() == 'youtube':
            count_youtube = count_youtube + 1
            total_income_youtube = total_income_youtube + int(income)
            total_age_youtube = total_age_youtube + int(age)
            dataset_income_youtube.append(int(income))
            dataset_age_youtube.append(int(age))
    
    # Sorting the list of unique countries alphabetically
    unique_countries_sorted = sorted(unique_countries)
    
    # Calculating the average time spent for the third output
    avg_time = total_time / count_people if count_people > 0 else 0
    
    # Calculating the standard deviation for the third output
    avg_income = total_income / count_people if count_people > 0 else 0
    variance = sum([(x - avg_income) ** 2 for x in dataset_income]) / (count_people - 1) if count_people - 1 > 0 else 0
    std_dev = variance ** 0.5
    
    # Calculating averages for the spent time for each of the demographics
    avg_urban = total_urban / count_urban if count_urban > 0 else 0
    avg_sub_urban = total_sub_urban / count_sub_urban if count_sub_urban > 0 else 0
    avg_rural = total_rural / count_rural if count_rural > 0 else 0
    
    # Comparing to identify the minimum average, and sorting alphabetically in case of equal minimums
    if avg_urban < avg_sub_urban and avg_urban < avg_rural:
        lowest_demography = 'Urban'
        if avg_urban == avg_sub_urban:
            lowest_demography = sorted(['Urban', 'Sub_Urban'])[0]
        elif avg_urban == avg_rural:
            lowest_demography = sorted(['Urban', 'Rural'])[0]
    
    elif avg_sub_urban < avg_urban and avg_sub_urban < avg_rural:
        lowest_demography = 'Sub_Urban'
        if avg_sub_urban == avg_urban:
            lowest_demography = sorted(['Sub_Urban', 'Urban'])[0]
        elif avg_sub_urban == avg_rural:
            lowest_demography = sorted(['Sub_Urban', 'Rural'])[0]
    
    elif avg_rural < avg_urban and avg_rural < avg_sub_urban:
        lowest_demography = 'Rural'
        if avg_rural == avg_urban:
            lowest_demography = sorted(['Rural', 'Urban'])[0]
        elif avg_rural == avg_sub_urban:
            lowest_demography = sorted(['Rural', 'Sub_Urban'])[0]
    
    elif avg_urban == avg_sub_urban == avg_rural:
        lowest_demography = sorted(['Urban', 'Sub_Urban', 'Rural'])[0]
    
    # Calculating average ages for each platform users
    avg_age_facebook = total_age_facebook / count_facebook if count_facebook > 0 else 0
    avg_age_instagram = total_age_instagram / count_instagram if count_instagram > 0 else 0
    avg_age_youtube = total_age_youtube / count_youtube if count_youtube > 0 else 0
    
    # Calculating average incomes for each platform users
    avg_income_facebook = total_income_facebook / count_facebook if count_facebook > 0 else 0
    avg_income_instagram = total_income_instagram / count_instagram if count_instagram > 0 else 0
    avg_income_youtube = total_income_youtube / count_youtube if count_youtube > 0 else 0
    
    # Comparing number of users to identify the platform with the highest amount of users, and sorting alphabetically in case of equal values
    if count_facebook > count_instagram and count_facebook > count_youtube:
        dataset_age_highest_platform = dataset_age_facebook
        dataset_income_highest_platform = dataset_income_facebook
        avg_age_highest_platform = avg_age_facebook
        avg_income_highest_platform = avg_income_facebook
        count_highest_platform = count_facebook
        if count_facebook == count_instagram or count_facebook == count_youtube:
            dataset_age_highest_platform = dataset_age_facebook
            dataset_income_highest_platform = dataset_income_facebook
            avg_age_highest_platform = avg_age_facebook
            avg_income_highest_platform = avg_income_facebook
            count_highest_platform = count_facebook
    
    elif count_instagram > count_facebook and count_instagram > count_youtube:
        dataset_age_highest_platform = dataset_age_instagram
        dataset_income_highest_platform = dataset_income_instagram
        avg_age_highest_platform = avg_age_instagram
        avg_income_highest_platform = avg_income_instagram
        count_highest_platform = count_instagram
        if count_instagram == count_facebook:
            dataset_age_highest_platform = dataset_age_facebook
            dataset_income_highest_platform = dataset_income_facebook
            avg_age_highest_platform = avg_age_facebook
            avg_income_highest_platform = avg_income_facebook
            count_highest_platform = count_facebook
        elif count_instagram == count_youtube:
            dataset_age_highest_platform = dataset_age_instagram
            dataset_income_highest_platform = dataset_income_instagram
            avg_age_highest_platform = avg_age_instagram
            avg_income_highest_platform = avg_income_instagram
            count_highest_platform = count_instagram
    
    elif count_youtube > count_facebook and count_youtube > count_instagram:
        dataset_age_highest_platform = dataset_age_youtube
        dataset_income_highest_platform = dataset_income_youtube
        avg_age_highest_platform = avg_age_youtube
        avg_income_highest_platform = avg_income_youtube
        count_highest_platform = count_youtube
        if count_youtube == count_facebook:
            dataset_age_highest_platform = dataset_age_facebook
            dataset_income_highest_platform = dataset_income_facebook
            avg_age_highest_platform = avg_age_facebook
            avg_income_highest_platform = avg_income_facebook
            count_highest_platform = count_facebook
        elif count_youtube == count_instagram:
            dataset_age_highest_platform = dataset_age_instagram
            dataset_income_highest_platform = dataset_income_instagram
            avg_age_highest_platform = avg_age_instagram
            avg_income_highest_platform = avg_income_instagram
            count_highest_platform = count_instagram
    
    # Calculating the numerator
    for i in range(count_highest_platform):
        numerator = numerator + (dataset_age_highest_platform[i] - avg_age_highest_platform) * (dataset_income_highest_platform[i] - avg_income_highest_platform)
    
    # Calculating the denominator
    denominator_age = sum((age_i - avg_age_highest_platform) ** 2 for age_i in dataset_age_highest_platform)
    denominator_income = sum((income_i - avg_income_highest_platform) ** 2 for income_i in dataset_income_highest_platform)
    denominator = (denominator_age ** 0.5) * (denominator_income ** 0.5)
    
    # Calculating the correlation
    correlation = numerator / denominator if denominator > 0 else 0
    
    # Defining the outputs
    OP1 = student_details
    OP2 = unique_countries_sorted
    OP3 = [round(avg_time, 4), round(std_dev, 4), lowest_demography.lower()]
    OP4 = round(correlation, 4)
    
    # Returning the outputs
    return OP1, OP2, OP3, OP4