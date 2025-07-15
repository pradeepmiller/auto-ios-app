import os
import re
import sys

class RedundantValueException(Exception):
    """Custom exception for redundant constant values."""
    def __init__(self, redundant_values):
        self.redundant_values = redundant_values
        message = "Redundant values found:\n" + "\n".join(
            [f" ->  Value - '{value}' is used in enums: {', '.join(enums)}" for value, enums in redundant_values.items()]
        )
        super().__init__(message)

def find_and_convert_swift_files(parent_folder, output_java_file):
    # Regex patterns
    file_name_pattern = re.compile(r"AccessibilityIdentifiers")
    case_pattern = re.compile(r"case (\w+) = \"([^\"]+)\"")
    enum_pattern = re.compile(r"enum (\w+):")

    # Java file content
    java_content = []
    java_content.append("/*")
    java_content.append(" * Auto-generated Java file from Swift Accessibility Identifiers for iOS platform")
    java_content.append(" */")
    java_content.append("public class AutomationIdLocatorsForIos {")
    java_content.append("")

    # Track processed enums and constants to avoid redundancy
    processed_enums = {}
    value_to_enums = {}

    # Walk through the parent folder
    for root, _, files in os.walk(parent_folder):
        for file in files:
            if file.endswith(".swift") and file_name_pattern.search(file):
                swift_file_path = os.path.join(root, file)
                with open(swift_file_path, "r") as swift_file:
                    lines = swift_file.readlines()

                current_enum = None
                for line in lines:
                    line = line.strip()

                    # Match enum declarations
                    enum_match = enum_pattern.match(line)
                    if enum_match:
                        current_enum = enum_match.group(1)
                        # Initialize the enum in the processed_enums dictionary if not already present
                        if current_enum not in processed_enums:
                            processed_enums[current_enum] = set()
                        continue

                    # Match case declarations
                    case_match = case_pattern.match(line)
                    if case_match and current_enum:
                        constant_name = case_match.group(1)
                        constant_value = case_match.group(2)

                        # Track constant values across enums
                        if constant_value in value_to_enums:
                            value_to_enums[constant_value].add(current_enum)
                        else:
                            value_to_enums[constant_value] = {current_enum}

                        # Add the constant to the current enum
                        processed_enums[current_enum].add(constant_value)

    # Check for redundancies
    redundant_values = {value: enums for value, enums in value_to_enums.items() if len(enums) > 1}
    if redundant_values:
        raise RedundantValueException(redundant_values)

    # Generate Java content from processed enums
    for enum_name, constants in processed_enums.items():
        java_content.append(f"    public static class {enum_name} {{")
        for constant_value in constants:
            # Generate a constant name from the value (e.g., button_close -> BUTTON_CLOSE)
            constant_name = constant_value.upper().replace(" ", "_").replace("-", "_")
            java_content.append(f"        public static final String {constant_name} = \"{constant_value}\";")
        java_content.append("    }")
        java_content.append("")

    # Close the main Java class
    java_content.append("}")

    # Write to the output Java file
    with open(output_java_file, "w") as java_file:
        java_file.write("\n".join(java_content))

    print(f"\033[32mJava file '{output_java_file}' has been generated successfully.\033[0m")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python scripts/swift_to_java_converter.py <parent_folder> <output_java_file>")
        sys.exit(1)
    parent_folder = sys.argv[1]
    output_java_file = sys.argv[2]
    try:
        find_and_convert_swift_files(parent_folder, output_java_file)
    except RedundantValueException as e:
        print(f"\033[91mError: {e}\033[0m")
      
