package kafka

import (
	"context"

	"github.com/confluentinc/confluent-kafka-go/kafka"
)

type Movie struct {
	producer *kafka.Producer
	topic    string
}

// instantiates a new movie
func NewMovie(producer *kafka.Producer, topic string) *Movie {

	return &Movie{
		producer: producer,
		topic:    topic,
	}

}

func (m *Movie) Created(ctx context.Context, movie Movie) {

}
