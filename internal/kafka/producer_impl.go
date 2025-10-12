package kafka

import (
	"bytes"
	"context"
	"encoding/json"
	"movie-api/internal"
	"movie-api/internal/models"

	"github.com/confluentinc/confluent-kafka-go/v2/kafka"
)

type movieProducer struct {
	producer  *kafka.Producer
	topicName string
}

type event struct {
	Type  string
	Value models.Movie
}

func NewMovieProducer(producer *kafka.Producer, topicName string) MovieProducer {
	return &movieProducer{
		producer:  producer,
		topicName: topicName,
	}
}

func (m *movieProducer) Created(ctx context.Context, movie models.Movie) error {
	return m.publish(ctx, "Movie.Created", movie)
}

func (m *movieProducer) Deleted(ctx context.Context, id string) error {
	return m.publish(ctx, "Movie.Deleted", models.Movie{ID: id})
}

func (m *movieProducer) Updated(ctx context.Context, movie models.Movie) error {
	return m.publish(ctx, "Movie.Updated", movie)
}

func (m *movieProducer) publish(_ context.Context, msgType string, movie models.Movie) error {
	var b bytes.Buffer

	evt := event{
		Type:  msgType,
		Value: movie,
	}

	if err := json.NewEncoder(&b).Encode(evt); err != nil {
		return internal.WrapErrorf(err, internal.ErrorCodeUnknown, "json.Encode")
	}

	if err := m.producer.Produce(&kafka.Message{
		TopicPartition: kafka.TopicPartition{
			Topic:     &m.topicName,
			Partition: kafka.PartitionAny,
		},
		Value: b.Bytes(),
	}, nil); err != nil {
		return internal.WrapErrorf(err, internal.ErrorCodeUnknown, "producer.Produce")
	}

	return nil
}
