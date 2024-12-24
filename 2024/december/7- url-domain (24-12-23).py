#problem from codewar
"""
Write a function that when given a URL as a string, parses out just the domain name and returns it as a string. 
For example:
      test.assert_equals(domain_name("http://google.com"), "google")
      test.assert_equals(domain_name("http://google.co.jp"), "google")
      test.assert_equals(domain_name("https://123.net"), "123")
      test.assert_equals(domain_name("https://hyphen-site.org"), "hyphen-site")
      test.assert_equals(domain_name("http://codewars.com"), "codewars")
      test.assert_equals(domain_name("www.xakep.ru"), "xakep")
      test.assert_equals(domain_name("https://youtube.com"), "youtube")
      test.assert_equals(domain_name("http://www.codewars.com/kata/"), "codewars")
      test.assert_equals(domain_name("icann.org"), "icann")
"""

#What I think I gonna do
"""
to split url in all case to evaluate and return the domain
i think i can use regular expression but is more work than split url
"""

#First implementation
"""
def domain_name(url):
   try:
      return url.split('//')[1].split('.')[0] if 'www' not in url else url.split('.')[1]
   except Exception as e:
      return url.split('.')[0]
"""
      
#clean code
def domain_name(url):
   return url.split("//")[-1].split("www.")[-1].split(".")[0]


print(domain_name("icann.org"))