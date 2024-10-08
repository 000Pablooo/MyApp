import requests
from bs4 import BeautifulSoup
import time
import re
from datetime import datetime


def script():
	url='https://www.yallakora.com/match-center/%d9%85%d8%b1%d9%83%d8%b2-%d8%a7%d9%84%d9%85%d8%a8%d8%a7%d8%b1%d9%8a%d8%a7%d8%aa'
	
	page=requests.get(url)
	
	def main(page):
		
		src=page.content
		soup=BeautifulSoup(src,'html.parser') 
		match_detiles=[]
		championship=soup.find_all("div",{'class':"matchCard"})
		def getmatch(championship):
  	#<----------- name match ------------>
			title=championship.contents[1].find('h2').text.strip()
			aa.append(f'{title:_^40}')
			all_match =championship.contents[3].find_all('div',{'class':'liItem'})
			#<--------TOP---------->
			nmber=len(all_match)
			for i in range(nmber):
			
	#	<---------- TEM    A   B ------------->'
				
				temA=all_match[i].find("div",{'class':'teamA'}).find('p').text.strip()
		
				temB=all_match[i].find("div",{'class':'teamB'}).find('p').text.strip()
		
		#          <--------نتيجة المبارات ---------->'
				
				match_re=all_match[i].find("div",{'MResult'}).find_all('span',{"class":"score"})
				score=f' {match_re[0].text.strip()} : {match_re[1].text.strip()} '
		#<---------موعد المبارات ------------->	
				match_time=all_match[i].find("div",{'MResult'}).find('span',{"class":"time"}).text.strip()
			
				toot=f'{temA}  {score}  {temB} ({match_time})'
				aa.append(toot)

			match=f'{title}\n{toot}'
		for i in range(len(championship)):
			getmatch(championship[i])
				
	aa=[]
	main(page)
	
	#match=''
#	match +='\n\n'.join(aa)

#<=============TMZ===============>
	response = requests.get('http://worldclockapi.com/api/json/utc/now')
	if response.status_code == 200:
	       data = response.json()
	       current_datetime_str = data['currentDateTime']
	       
	       current_datetime = datetime.fromisoformat(current_datetime_str.replace("Z", "+00:00"))
	       formatted_datetime = current_datetime.strftime("%d/%m/%Y >> %H:%M")
	       
	       time=(f"{formatted_datetime}")
	else:
		time=("time")
	
	
	match=f'🌍🕑 :      {time}\n\n'
	match +='\n\n'.join(aa)

#===============PST=================>
	
	
	cookies="datr=CnIBZxfadzn-JH0lxCnkEbYi; ps_l=1; ps_n=1; sb=CnIBZ2Mt3yLd9F-DZ6REiAXT; m_pixel_ratio=1.75; wd=412x732; c_user=100084030874274; fr=0YoUGFFLs1ponTgXw.AWWU-aZ-FfKyMYEo-sFLEqFBmKI.BnAXIK..AAA.0.0.BnAXI_.AWWyMNZj5EA; xs=20%3AlhD7U4ltN5iyrA%3A2%3A1728148032%3A-1%3A12235; vpd=v1%3B732x412x1.75; i_user=61566479923664; locale=en_US; fbl_st=101521820%3BT%3A28802467; wl_cbv=v2%3Bclient_version%3A2635%3Btimestamp%3A1728148057"
	
	session=requests.Session()
	headers = {"user-agent":"Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Mobile Safari/537.36 [FBAN/EMA;FBLC/ar_AR;FBAV/370.0.0.16.116;FBDM/DisplayMetrics{density=1.6, width=720, height=1352, scaledDensity=1.6, xdpi=294.967, ydpi=294.967, densityDpi=256, noncompatWidthPixels=720, noncompatHeightPixels=1352, noncompatDensity=1.6, noncompatDensityDpi=256, noncompatXdpi=294.967, noncompatYdpi=294.967};]",'Cookie':cookies}
	
	
	
	url ='https://m.facebook.com'
	
	res=session.get(url,headers=headers).text
	
	
	form = re.search('<form method="post" action="(.+)',res).group()
	
	
	action=re.search('<form method="post" action="(.+?)"',form).group(1)
	
	data={'fb_dtsg':re.search('input type="hidden" name="fb_dtsg" value="(.+?)"',form).group(1),'jazoest':re.search('input type="hidden" name="jazoest" value="(.+?)"',form).group(1),'xc_message':match,'view_post':'نشر'}
	
	
	url=f'https://m.facebook.com{action}'
	
	response=session.post(url,data=data,headers=headers).text
	
while True:
	script()
	time.sleep(1800)