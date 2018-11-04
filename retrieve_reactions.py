import urllib2
import json
import logging
import traceback
import datetime
import os.path

try:
    logging.basicConfig(filename='\PATH\TO\post_to_fb.log', level=logging.INFO)

    with open('\PATH\TO\config_params2.json','r') as input_file:
            logging.info("Parsing config file")
            input_json_string=input_file.read().replace('\n','')
            json_arr=json.loads(input_json_string)

    json_arr=[]

    urlStr="https://graph.facebook.com/v2.10/%d_%d?access_token=%s&fields=created_time,story,message,shares,reactions.type(LIKE).limit(0).summary(1).as(like),reactions.type(LOVE).limit(0).summary(1).as(love),reactions.type(HAHA).limit(0).summary(1).as(haha),reactions.type(WOW).limit(0).summary(1).as(wow),reactions.type(SAD).limit(0).summary(1).as(sad),reactions.type(ANGRY).limit(0).summary(1).as(angry)&limit=10"%(json_arr['fb_page_id'],json_arr['post_id'],json_arr['fb_access_token'].strip())
                            logging.info(urlStr)
                            req=urllib2.Request(urlStr)

                            logging.info(req)

                            response = urllib2.urlopen(req)

                            obj=json.loads(response.read())

                            logging.info(obj)
                            share_count=0 if 'shares' not in obj else obj['shares']['count']
                            logging.info("Share count: " + str(share_count))
                            logging.info("Like count : " + str(obj['like']['summary']['total_count']))
                            logging.info("Love count : " + str(obj['love']['summary']['total_count']))
except:
        logging.info("ERROR")
        logging.info(traceback.format_exc())