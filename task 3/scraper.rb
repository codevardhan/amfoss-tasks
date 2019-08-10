require ‘nokogiri’
require ‘open-uri’
require ‘pry’

doc = Nokogiri::HTML(open(‘https://www.google.com/search?q=linux&ie=&oe='))