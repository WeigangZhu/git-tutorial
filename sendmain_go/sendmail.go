// use Go to send a email

package main

import (
    "fmt"
    "net/smtp"
    "strings"
)

func main() {
    auth := smtp.PlainAuth("", "2216859338@qq.com", "oqzjvolpxudrdjge", "smtp.qq.com")
    to := []string{"809684907@qq.com"}
    nickname := "test"
    user := "2216859338@qq.com"
    subject := "Hello, world"
    content_type := "Content-Type: text/plain; charset=UTF-8"
    body := "Welcom the world! This is the new wrold with GO. This is the email body."
    
    msg := []byte("To: " + strings.Join(to, ",") + "\r\n" +
    			  "From: " + nickname + "<" + user + ">\r\n" +
    			  "Subject: " + subject + "\r\n" + 
    			   content_type + "\r\n\r\n" +  
    			   body)
        
    err := smtp.SendMail("smtp.qq.com:25", auth, user, to, msg)
    
    if err != nil {
        fmt.Printf("send mail error: %v", err)
    }
}
