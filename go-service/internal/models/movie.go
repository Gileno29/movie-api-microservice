package models

type Movie struct {
	ID          string `json:"id"`
	Name        string `json:"name"`
	Description string `json:"description"`
	Genre       string `json:"genre"`
	Year        int    `json:"year"`
}
