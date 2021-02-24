#Yelp Call Function
def yelp_call(url_params):
    
    response = requests.get(url, headers=headers, params=url_params)
    return response.json()['businesses']

#Data Parsing Function
def parse_results(list_of_data):
    # create a container to hold our parsed data
    biz_list = []
    # loop through our business and 
    for business in list_of_data:
    # parse each individual business into a tuple
        try:
            biz_tuple = (business['name'],
                     business['location']['address1'],
                     business['rating'],
                     business['price'],
                     business['location']['zip_code'],
                     business['transactions'],
                     business['review_count'],
                     business['categories'])   
    # add each individual business tuple to our data container
            biz_list.append(biz_tuple)
        except:
            continue
    # return the container with all of the parsed results
    return biz_list

#Saving as CSV Function
def df_save(csv_file_path, parsed_results):
    # your code to open the csv file, concat the current data, and save the data. 
    business_df = pd.DataFrame(parsed_results, columns = ['Name', 'Location', 'Rating', 'Price', 'Zipcode', 'Transactions', 'Review Count', 'Categories'])
    business_df.to_csv(csv_file_path, mode = 'a')
    new_df = pd.read_csv(csv_file_path, delimiter = ",")
    return new_df    
