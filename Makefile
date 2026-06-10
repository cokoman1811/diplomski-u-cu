CC      ?= gcc
CFLAGS  ?= -std=c99 -O2 -Wall -Wextra -Isrc
LDFLAGS ?= -lm

SRC_DIR := src
BUILD_DIR := build
SOURCES := $(wildcard $(SRC_DIR)/*.c)
LIB_SOURCES := $(filter-out $(SRC_DIR)/main.c,$(SOURCES))
OBJECTS := $(patsubst $(SRC_DIR)/%.c,$(BUILD_DIR)/%.o,$(SOURCES))
LIB_OBJECTS := $(patsubst $(SRC_DIR)/%.c,$(BUILD_DIR)/%.o,$(LIB_SOURCES))
TARGET  := diplomski
TEST_TARGET := tests

.PHONY: all clean run test

all: $(TARGET)

$(TARGET): $(OBJECTS)
	$(CC) $(OBJECTS) -o $@ $(LDFLAGS)

$(TEST_TARGET): tests/run_tests.c $(LIB_OBJECTS)
	$(CC) $(CFLAGS) tests/run_tests.c $(LIB_OBJECTS) -o $@ $(LDFLAGS)

$(BUILD_DIR)/%.o: $(SRC_DIR)/%.c | $(BUILD_DIR)
	$(CC) $(CFLAGS) -c $< -o $@

$(BUILD_DIR):
	mkdir -p $(BUILD_DIR)

run: all
	./$(TARGET) --compare

test: $(TEST_TARGET)
	./$(TEST_TARGET)

clean:
	rm -rf $(BUILD_DIR) $(TARGET) $(TARGET).exe $(TEST_TARGET) $(TEST_TARGET).exe tests.exe
