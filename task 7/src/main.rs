extern crate regex;
use regex::Regex;

fn main() {
    println!("Enter the email id to be checked:");
    let mut mail = String::new();
    std::io::stdin().read_line(&mut mail).unwrap();
    if (Regex::new(r"\b[a-zA-Z0-9]+@[a-z][.]?[a-z]*").unwrap().is_match(&mut mail)) == true
    {
    	println!("Entered email is valid.");
    }
    else {
    	println!("Entered email is invalid.");
    }
}
