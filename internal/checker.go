package internal

import (
	"strings"
	"unicode"
)

type PasswordChecker interface {
	Check(string) (bool, string)
}

type LengthChecker struct{}

func (lc LengthChecker) Check(password string) (bool, string) {
	comment := ""
	if len(password) < 8 {
		comment = "- Twoje hasło musi składać się z przynajmniej 8 znaków."
		return false, comment
	}
	return true, comment
}

type WhitespaceChecker struct{}

func (wc WhitespaceChecker) Check(password string) (bool, string) {
	comment := ""
	for _, char := range password {
		if unicode.IsSpace(char) {
			comment = "- Twoje hasło NIE może zawierać spacji."
			return false, comment
		}
	}
	return true, comment
}

type UpperCharChecker struct{}

func (uc UpperCharChecker) Check(password string) (bool, string) {
	comment := ""
	for _, char := range password {
		if unicode.IsUpper(char) {
			return true, comment
		}
	}
	comment = "- Twoje hasło musi zawierać conajmniej jedną dużą literę."
	return false, comment
}

type LowerCharChecker struct{}

func (lc LowerCharChecker) Check(password string) (bool, string) {
	comment := ""
	for _, char := range password {
		if unicode.IsLower(char) {
			return true, comment
		}
	}
	comment = "- Twoje hasło musi zawierać conajmniej jedną małą literę."
	return false, comment
}

type SpecialCharChecker struct{}

func (sc SpecialCharChecker) Check(password string) (bool, string) {
	comment := ""
	specialChars := "!\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~"
	for _, char := range password {
		if strings.ContainsRune(specialChars, char) {
			return true, comment
		}
	}
	comment = "- Twoje hasło musi zawierać conajmniej jeden znak specjalny."
	return false, comment
}

type DigitChecker struct{}

func (dc DigitChecker) Check(password string) (bool, string) {
	comment := ""
	for _, char := range password {
		if unicode.IsDigit(char) {
			return true, comment
		}
	}
	comment = "- Twoje hasło musi zawierać conajmniej jedną cyfrę."
	return false, comment
}
