package main

import (
	"bufio"
	"fmt"
	"os"
	"password_security/internal"
	"strings"
)

func main() {
	reader := bufio.NewReader(os.Stdin)
	fmt.Print("Enter a password: ")
	password, _ := reader.ReadString('\n')
	password = strings.TrimSpace(password)

	checkers := []internal.PasswordChecker{
		internal.LengthChecker{},
		internal.UpperCharChecker{},
		internal.LowerCharChecker{},
		internal.DigitChecker{},
		internal.SpecialCharChecker{},
		internal.WhitespaceChecker{},
	}

	flag := true
	comment := "Password is safe."
	for _, checker := range checkers {
		if success, _ := checker.Check(password); !success {
			flag = false
			comment = "Your password is not safe enough."
			break
		}
	}

	fmt.Println(comment)

	if !flag {
		internal.AskForReport()

		for _, checker := range checkers {
			internal.PrepareReport(checker, password)
		}
	}
}
