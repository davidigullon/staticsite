from enum import Enum
import re

class BlockType(Enum):
    PARAGRAPH = "paragraph"
    HEADING = "heading"
    CODE = "code"
    QUOTE = "quote"
    UNORDERED_LIST = "unordered_list"
    ORDERED_LIST = "ordered_list"

def block_to_block_type(block: str) -> BlockType:
    lines = block.splitlines()

    if lines[0] == "```" and lines[-1] == "```" and len(lines) >= 2:
        return BlockType.CODE
    
    if len(lines) == 1 and re.match(r'#{1,6} ', lines[0]):
        return BlockType.HEADING
    
    if all(line.startswith("- ") for line in lines):
        return BlockType.UNORDERED_LIST
    
    if all(line.startswith("> ") or line == ">" for line in lines):
        return BlockType.QUOTE
    
    ordered_pattern = re.compile(r"^(\d+)\. ")
    expected_number = 1
    is_ordered = True
    for line in lines:
        match = ordered_pattern.match(line)
        if not match or int(match.group(1)) != expected_number:
            is_ordered = False
            break
        expected_number += 1
    if is_ordered:
        return BlockType.ORDERED_LIST
    
    return BlockType.PARAGRAPH