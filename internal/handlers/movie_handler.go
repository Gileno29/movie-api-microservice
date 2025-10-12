package handlers

import (
	"fmt"
	"net/http"

	"movie-api/internal/models"
	"movie-api/internal/service"

	"github.com/gin-gonic/gin"
)

type MovieHandler struct {
	service service.MovieService
}

func NewMovieHandler(service service.MovieService) *MovieHandler {
	return &MovieHandler{service: service}
}

func (h *MovieHandler) CreateMovie(c *gin.Context) {
	var movie models.Movie

	fmt.Println(c.Request.Body)

	if err := c.ShouldBindJSON(&movie); err != nil {
		c.JSON(http.StatusBadRequest, gin.H{"error to bind in json": err.Error()})
		return
	}

	if err := h.service.CreateMovie(c.Request.Context(), &movie); err != nil {
		c.JSON(http.StatusInternalServerError, gin.H{"error to create a movie": err.Error()})
		return
	}

	c.JSON(http.StatusCreated, movie)
}
