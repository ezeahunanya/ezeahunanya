Title: First time for everything (Marvel Cinematic Universe Movie Ratings)
Date: 2020-11-22 17:39
Modified: 2020-12-03 23:16
Category: Blog
Tags: python, data science, pelican, publishing
Slug: first_time_for_everything
Author: Eze Ahunanya
Summary: This is new. Writing a blog. Who would have thought it? Not me. But here we are.

This is new. Writing a blog. Who would have thought it? Not me. But here we are.

My story starts as a fresh graduate with a master's degree from Loughborough
University. A master of Chemical Engineering apparently, but zero ideas of what I
wanted to do. After stumbling for the better part of a year, I came across data
science while researching my career options. An area which seemed
interesting and suitable with my interests and transferable skills. I decided
to learn Python to improve my technical coding skills and help me
break into data science. With a recommendation from a friend of a friend, I
completed Udacity's Data Analyst Nanodegree. I also completed a few projects
in the process which gave me a solid understanding of Python. Then covid-19
hit the world and the lockdown with it. Things slowed down for me but I made
sure to keep practising.

To knock off some rust, I decided to do an independent project. And with talks
of an impending second lockdown, I wanted the project to be movie related as I
knew a lot my friends spent a significant amount of time on streaming platforms
in the first lockdown. As I thoroughly enjoyed the movies in the marvel
cinematic universe the choice was pretty obvious to me.

The first challenge I faced, was gathering the data. I knew I could
find the relevant data on the RottenTomatoes website but I had never scraped
data off the internet before. To combat this, I had to get acquainted with
Beautiful Soup's documentation very quickly. For those who do not know,
Beautiful Soup is a Python package which acts HTML parser and is used to decode
HTML code and extract data. After a solid week of trial and error, I finally
wrote a working function to extract the data for each MCU movie and combine
it into one DataFrame. The function collected the movie titles, the audience
and critics scores, box office figures, runtime, and the release date. The code
looked like this:  

    #!python
    def get_movie_data(urls_list):

        """Get the movie data from its url.

        Arg:
        url: URL link containing movie data. This should be from Rotten Tomatoes
        and in a list.

        Returns:
        df: A dataframe containing movie data."""

        for i, url in enumerate(urls_list):
            if i == 0:
                # save html file in respone variable
                response = requests.get(url)
                soup = BeautifulSoup(response.content, 'lxml')

                # extract scores data as dictionary
                scores_text = (soup.find_all('script', type=
                                              'text/javascript')[2].text)
                scores_text_lines_list = scores_text.split('\n')
                for line in scores_text_lines_list:
                    if 'root.RottenTomatoes.context.scoreInfo' in line:
                        scores_data_dict = line
                        break
                scores_data_dict = (scores_data_dict.replace('root.RottenTomatoes'
                                    '.context.scoreInfo = ', '').replace('true',
                                    'True').replace('false', 'False').replace('null',
                                    'np.nan')[:-1])

                # convert dictionary into the first dataframe
                df = (pd.DataFrame.from_dict(eval(scores_data_dict),
                     orient='index').reset_index())

                # extract other movie info and add to the dataframe
                movie_title = soup.title.text[:-len(' - Rotten Tomatoes')]
                df['movie_title'] = pd.Series([movie_title] * len(df['index']))
                release_date_theaters = (soup.find_all('li', class_='meta-row '
                                        'clearfix')[6].contents[3].contents[1].text)
                df['release_date_theaters'] = (pd.Series([release_date_theaters]
                                              * len(df['index'])))
                box_office_gross_usa = soup.find_all('li', class_='meta-row '
                                       'clearfix')[8].contents[3].text
                df['box_office_gross_usa'] = (pd.Series([box_office_gross_usa]
                                             * len(df['index'])))
                runtime = (soup.find_all('li', class_='meta-row clearfix')[9]
                          .contents[3].text.split('\n')[2].replace(' ', ''))
                df['runtime'] = pd.Series([runtime] * len(df['index']))
This block of code was repeated for the second URL and following ones.
The results were concatenated together in one DataFrame.

The next challenge came when I started cleaning the data. For the Avengers the
box office number was not provided on the website. So the runtime was pulled in
box office column and the runtime column had irrelevant information. This is
because the code indexed the certain areas assuming the structure would be the
same on every RottenTomatoes page. The relevant section of the code is (taken
from line 35-48):  

    :::python
    # extract other movie info and add to the dataframe
    movie_title = soup.title.text[:-len(' - Rotten Tomatoes')]
    df['movie_title'] = pd.Series([movie_title] * len(df['index']))
    release_date_theaters = (soup.find_all('li', class_='meta-row '
                            'clearfix')[6].contents[3].contents[1].text)
    df['release_date_theaters'] = (pd.Series([release_date_theaters]
                                  * len(df['index'])))
    box_office_gross_usa = soup.find_all('li', class_='meta-row '
                           'clearfix')[8].contents[3].text
    df['box_office_gross_usa'] = (pd.Series([box_office_gross_usa]
                                 * len(df['index'])))
    runtime = (soup.find_all('li', class_='meta-row clearfix')[9]
              .contents[3].text.split('\n')[2].replace(' ', ''))
    df['runtime'] = pd.Series([runtime] * len(df['index']))  
For the box office figure, the code indexed the 9th element of the results
returned from the find_all method. For the runtime, the code indexed the 10th
element. In the unique case of The Avengers, there was no box office figure so
the 9th element had the runtime information.

To fix this, I had to figure out how to make the code search for specific movie
attributes and put them into the correct columns. I did consider scrapping the
box office column which had the problem to avoid it altogether. But I love
a good challenge. After a day or two, I solved the issue by searching for
the attribute name before pulling the data. The more robust code looks like
this:

    :::python
    # extract release date and add to dataframe   
    for i in[i for i in range(0, max_limit)]:
        li_tag_line = soup.find_all('li', class_='meta-row clearfix')[i]
        li_descendants = list(li_tag_line.descendants)
        if 'Release Date (Theaters):' in li_descendants:
            release_date_theaters = li_descendants[7]
            break
        else:
            release_date_theaters = np.nan

    df['release_date_theaters'] = (pd.Series([release_date_theaters]
                                              * len(df.index)))

    # extract runtime and add to dataframe
    for i in[i for i in range(0, max_limit)]:
        li_tag_line = soup.find_all('li', class_='meta-row clearfix')[i]
        li_descendants = list(li_tag_line.descendants)
        if 'Runtime:' in li_descendants:
            runtime = li_descendants[7].split('\n')[1]
            break
        else:
            runtime = np.nan

    df['runtime'] = pd.Series([runtime] * len(df.index))

    # extract box office info and add to dataframe
    for i in[i for i in range(0, max_limit)]:
        li_tag_line = soup.find_all('li', class_='meta-row clearfix')[i]
        li_descendants = list(li_tag_line.descendants)
        if 'Box Office (Gross USA):' in li_descendants:
            box_office_gross_usa = li_descendants[5]
            break
        else:
            box_office_gross_usa = np.nan

    df['box_office_gross_usa'] = (pd.Series([box_office_gross_usa]
                                             * len(df.index)))

After the data was collected, the rest was smooth sailing. I used Tableau to
visualise the data because I wanted to have an interactive chart. This was the
result:
<center>
<div class='tableauPlaceholder' id='viz1606736942644' style='position: relative'><noscript><a href='#'><img alt=' ' src='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;Be&#47;BestofMCUMovies&#47;Story1&#47;1_rss.png' style='border: none' /></a></noscript><object class='tableauViz'  style='display:none;'><param name='host_url' value='https%3A%2F%2Fpublic.tableau.com%2F' /> <param name='embed_code_version' value='3' /> <param name='site_root' value='' /><param name='name' value='BestofMCUMovies&#47;Story1' /><param name='tabs' value='no' /><param name='toolbar' value='yes' /><param name='static_image' value='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;Be&#47;BestofMCUMovies&#47;Story1&#47;1.png' /> <param name='animate_transition' value='yes' /><param name='display_static_image' value='yes' /><param name='display_spinner' value='yes' /><param name='display_overlay' value='yes' /><param name='display_count' value='yes' /><param name='language' value='en' /></object></div><script type='text/javascript'>                    var divElement = document.getElementById('viz1606736942644');                    var vizElement = divElement.getElementsByTagName('object')[0];                    vizElement.style.width='1016px';vizElement.style.height='991px';                    var scriptElement = document.createElement('script');                    scriptElement.src = 'https://public.tableau.com/javascripts/api/viz_v1.js';                    vizElement.parentNode.insertBefore(scriptElement, vizElement);                </script>  
</center>  

Once I finished the project, I decided to write a blog about the process. I
also figured that a website to host this blog and future blogs would be a neat
touch. I have never made a website before so I guess I have a bit of learning
to do, then a lot of work. Anyways, not bad for my first blog. P.S. If you are
reading this, mission complete.
