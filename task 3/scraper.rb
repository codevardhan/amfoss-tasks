require 'nokogiri'
require 'open-uri'

class Scraper
   puts "Enter word that you want to search. "
   search = gets
   doc = Nokogiri::HTML(open("https://www.google.com/search?q=#{search}&ie=&oe="))
   a = []
   link = []
   heading = []
   doc.xpath("//a/div").each do |link|
      a.push(link.text)
   end
   for i in 0..a.length
      if a[i] != nil AND a[i].include? "https://"
            link.push(a[i])
            heading.push(a[i-1])
      end
   end
   for j in 0..link.length
      puts heading[j]
      puts link[j]
      puts " "
   end
end
Scraper
