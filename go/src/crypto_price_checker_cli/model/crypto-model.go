package model

import "fmt"

type CryptoResponse []struct {
	Name              string `json:"name"`
	Price             string `json:"price"`
	Rank              string `json:"rank"`
	CirculatingSupply string `json:"circulating_supply"`
}

func (c CryptoResponse) TextOutput() string {
	p := fmt.Sprintf(
		"Name: %s\nPrice : %s\nRank: %s\nCirculatingSupply: %s\n",
		c[0].Name, c[0].Price, c[0].Rank, c[0].CirculatingSupply)
	return p
}
