"""Functions for the December 6 task."""


def _find_marker(input: str, marker_length: int) -> int:
    for i, _ in enumerate(input):
        if len(set(input[i : i + marker_length])) == marker_length:
            return i + marker_length
    return 0


def find_packet_marker(input: str) -> int:
    return _find_marker(input, 4)


def find_message_marker(input: str) -> int:
    return _find_marker(input, 14)


if __name__ == "__main__":
    with open("december6_input.txt") as file:
        december6_signal = file.read()
    print(
        "How many characters need to be processed before the first start-of-packet marker is detected? ",
        find_packet_marker(december6_signal),
    )
    print(
        "How many characters need to be processed before the first start-of-message marker is detected?",
        find_message_marker(december6_signal),
    )
