package service

import (
	"context"
	"movie-api/internal/kafka"
	"movie-api/internal/models"
)

type MovieService interface {
	CreateMovie(ctx context.Context, movie *models.Movie) error
}

type movieService struct {
	kafkaProducer kafka.MovieProducer
}

func NewMovieService(kafkaProducer kafka.MovieProducer) MovieService {
	return &movieService{kafkaProducer: kafkaProducer}
}

func (s *movieService) CreateMovie(ctx context.Context, movie *models.Movie) error {
	return s.kafkaProducer.Created(ctx, *movie)
}
