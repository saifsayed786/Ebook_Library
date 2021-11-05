package client

import (
	"crypto_price_checker_cli/model"
	"encoding/json"
	"log"
	"net/http"
)

func FetchCrypto(fiat string, crypto string) (string, error) {
	//Build The URL string
	URL := "https://api.nomics.com/v1/currencies/ticker?key=3990ec554a414b59dd85d29b2286dd85&interval=1d&ids=" + crypto + "&convert=" + fiat

	resp, err := http.Get(URL)
	if err != nil {
		log.Fatal("oooops an error occured ! ")
	}
	defer resp.Body.Close()
	var cResp model.CryptoResponse
	if err := json.NewDecoder(resp.Body).Decode(&cResp); err != nil {
		log.Fatal("ooopsss an error occurred ! ")
	}
	return cResp.TextOutput(), nil
}
