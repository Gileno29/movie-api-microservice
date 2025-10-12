package kafka

import (
	"context"
	"movie-api/internal/models"
)

type MovieProducer interface {
	Created(ctx context.Context, movie models.Movie) error
	Deleted(ctx context.Context, id string) error
	Updated(ctx context.Context, movie models.Movie) error
}
