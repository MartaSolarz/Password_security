package internal

import (
	"bufio"
	"fmt"
	"os"
	"strings"
)

func AskForReport() {
	reader := bufio.NewReader(os.Stdin)
	for {
		fmt.Print("Do you want to see advices? [y/n] ")
		text, _ := reader.ReadString('\n')
		text = strings.TrimSpace(text)
		if text == "y" {
			break
		} else if text == "n" {
			os.Exit(1)
		} else {
			fmt.Println("Invalid value. Enter [y/n].")
		}
	}
}

func PrepareReport(checker PasswordChecker, password string) {
	flag, comment := checker.Check(password)
	if !flag {
		fmt.Println(comment)
	}
}
