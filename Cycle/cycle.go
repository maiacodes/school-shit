package main

import "github.com/sirupsen/logrus"

func main() {
	x := 1

	for true {
		x = x + 1
		logrus.Info(x)
	}
}
