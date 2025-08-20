# NOTE: This file has been automatically generated, do not modify!
# Architecture based on https://github.com/mrexodia/ida-pro-mcp (MIT License)
import sys
if sys.version_info >= (3, 12):
    from typing import Annotated, Optional, TypedDict, Generic, TypeVar, NotRequired
else:
    from typing_extensions import Annotated, Optional, TypedDict, Generic, TypeVar, NotRequired
from pydantic import Field

T = TypeVar("T")

class Metadata(TypedDict):
    path: str
    module: str
    base: str
    size: str
    md5: str
    sha256: str
    crc32: str
    filesize: str

class Function(TypedDict):
    address: str
    name: str
    size: str

class ConvertedNumber(TypedDict):
    decimal: str
    hexadecimal: str
    bytes: str
    ascii: Optional[str]
    binary: str

class Page(TypedDict, Generic[T]):
    data: list[T]
    next_offset: Optional[int]

class Global(TypedDict):
    address: str
    name: str

class Import(TypedDict):
    address: str
    imported_name: str
    module: str

class String(TypedDict):
    address: str
    length: int
    string: str

class DisassemblyLine(TypedDict):
    segment: NotRequired[str]
    address: str
    label: NotRequired[str]
    instruction: str
    comments: NotRequired[list[str]]

class Argument(TypedDict):
    name: str
    type: str

class DisassemblyFunction(TypedDict):
    name: str
    start_ea: str
    return_type: NotRequired[str]
    arguments: NotRequired[list[Argument]]
    stack_frame: list[dict]
    lines: list[DisassemblyLine]

class Xref(TypedDict):
    address: str
    type: str
    function: Optional[Function]

class StackFrameVariable(TypedDict):
    name: str
    offset: str
    size: str
    type: str

class StructureMember(TypedDict):
    name: str
    offset: str
    size: str
    type: str

class StructureDefinition(TypedDict):
    name: str
    size: str
    members: list[StructureMember]

@mcp.tool()
def get_metadata() -> Metadata:
    """Get metadata about the current IDB"""
    return make_jsonrpc_request('get_metadata')

@mcp.tool()
def get_function_by_name(name: Annotated[str, Field(description='Name of the function to get')]) -> Function:
    """Get a function by its name"""
    return make_jsonrpc_request('get_function_by_name', name)

@mcp.tool()
def get_function_by_address(address: Annotated[str, Field(description='Address of the function to get')]) -> Function:
    """Get a function by its address"""
    return make_jsonrpc_request('get_function_by_address', address)

@mcp.tool()
def get_current_address() -> str:
    """Get the address currently selected by the user"""
    return make_jsonrpc_request('get_current_address')

@mcp.tool()
def get_current_function() -> Optional[Function]:
    """Get the function currently selected by the user"""
    return make_jsonrpc_request('get_current_function')

@mcp.tool()
def convert_number(text: Annotated[str, Field(description='Textual representation of the number to convert')], size: Annotated[Optional[int], Field(description='Size of the variable in bytes')]) -> ConvertedNumber:
    """Convert a number (decimal, hexadecimal) to different representations"""
    return make_jsonrpc_request('convert_number', text, size)

@mcp.tool()
def list_functions(offset: Annotated[int, Field(description='Offset to start listing from (start at 0)')], count: Annotated[int, Field(description='Number of functions to list (100 is a good default, 0 means remainder)')]) -> Page[Function]:
    """List all functions in the database (paginated)"""
    return make_jsonrpc_request('list_functions', offset, count)

@mcp.tool()
def list_globals_filter(offset: Annotated[int, Field(description='Offset to start listing from (start at 0)')], count: Annotated[int, Field(description='Number of globals to list (100 is a good default, 0 means remainder)')], filter: Annotated[str, Field(description='Filter to apply to the list (required parameter, empty string for no filter). Case-insensitive contains or /regex/ syntax')]) -> Page[Global]:
    """List matching globals in the database (paginated, filtered)"""
    return make_jsonrpc_request('list_globals_filter', offset, count, filter)

@mcp.tool()
def list_globals(offset: Annotated[int, Field(description='Offset to start listing from (start at 0)')], count: Annotated[int, Field(description='Number of globals to list (100 is a good default, 0 means remainder)')]) -> Page[Global]:
    """List all globals in the database (paginated)"""
    return make_jsonrpc_request('list_globals', offset, count)

@mcp.tool()
def list_imports(offset: Annotated[int, Field(description='Offset to start listing from (start at 0)')], count: Annotated[int, Field(description='Number of imports to list (100 is a good default, 0 means remainder)')]) -> Page[Import]:
    """ List all imported symbols with their name and module (paginated) """
    return make_jsonrpc_request('list_imports', offset, count)

@mcp.tool()
def list_strings_filter(offset: Annotated[int, Field(description='Offset to start listing from (start at 0)')], count: Annotated[int, Field(description='Number of strings to list (100 is a good default, 0 means remainder)')], filter: Annotated[str, Field(description='Filter to apply to the list (required parameter, empty string for no filter). Case-insensitive contains or /regex/ syntax')]) -> Page[String]:
    """List matching strings in the database (paginated, filtered)"""
    return make_jsonrpc_request('list_strings_filter', offset, count, filter)

@mcp.tool()
def list_strings(offset: Annotated[int, Field(description='Offset to start listing from (start at 0)')], count: Annotated[int, Field(description='Number of strings to list (100 is a good default, 0 means remainder)')]) -> Page[String]:
    """List all strings in the database (paginated)"""
    return make_jsonrpc_request('list_strings', offset, count)

@mcp.tool()
def list_local_types():
    """List all Local types in the database"""
    return make_jsonrpc_request('list_local_types')

@mcp.tool()
def decompile_function(address: Annotated[str, Field(description='Address of the function to decompile')]) -> str:
    """Decompile a function at the given address"""
    return make_jsonrpc_request('decompile_function', address)

@mcp.tool()
def disassemble_function(start_address: Annotated[str, Field(description='Address of the function to disassemble')]) -> DisassemblyFunction:
    """Get assembly code for a function"""
    return make_jsonrpc_request('disassemble_function', start_address)

@mcp.tool()
def get_xrefs_to(address: Annotated[str, Field(description='Address to get cross references to')]) -> list[Xref]:
    """Get all cross references to the given address"""
    return make_jsonrpc_request('get_xrefs_to', address)

@mcp.tool()
def get_xrefs_to_field(struct_name: Annotated[str, Field(description='Name of the struct (type) containing the field')], field_name: Annotated[str, Field(description='Name of the field (member) to get xrefs to')]) -> list[Xref]:
    """Get all cross references to a named struct field (member)"""
    return make_jsonrpc_request('get_xrefs_to_field', struct_name, field_name)

@mcp.tool()
def get_callees(function_address: Annotated[str, Field(description='Address of the function to get callee functions')]) -> list[dict[str, str]]:
    """Get all the functions called (callees) by the function at function_address"""
    return make_jsonrpc_request('get_callees', function_address)

@mcp.tool()
def get_callers(function_address: Annotated[str, Field(description='Address of the function to get callers')]) -> list[Function]:
    """Get all callers of the given address"""
    return make_jsonrpc_request('get_callers', function_address)

@mcp.tool()
def get_entry_points() -> list[Function]:
    """Get all entry points in the database"""
    return make_jsonrpc_request('get_entry_points')

@mcp.tool()
def set_comment(address: Annotated[str, Field(description='Address in the function to set the comment for')], comment: Annotated[str, Field(description='Comment text')]):
    """Set a comment for a given address in the function disassembly and pseudocode"""
    return make_jsonrpc_request('set_comment', address, comment)

@mcp.tool()
def rename_local_variable(function_address: Annotated[str, Field(description='Address of the function containing the variable')], old_name: Annotated[str, Field(description='Current name of the variable')], new_name: Annotated[str, Field(description='New name for the variable (empty for a default name)')]):
    """Rename a local variable in a function"""
    return make_jsonrpc_request('rename_local_variable', function_address, old_name, new_name)

@mcp.tool()
def rename_global_variable(old_name: Annotated[str, Field(description='Current name of the global variable')], new_name: Annotated[str, Field(description='New name for the global variable (empty for a default name)')]):
    """Rename a global variable"""
    return make_jsonrpc_request('rename_global_variable', old_name, new_name)

@mcp.tool()
def set_global_variable_type(variable_name: Annotated[str, Field(description='Name of the global variable')], new_type: Annotated[str, Field(description='New type for the variable')]):
    """Set a global variable's type"""
    return make_jsonrpc_request('set_global_variable_type', variable_name, new_type)

@mcp.tool()
def get_global_variable_value_by_name(variable_name: Annotated[str, Field(description='Name of the global variable')]) -> str:
    """
    Read a global variable's value (if known at compile-time)

    Prefer this function over the `data_read_*` functions.
    """
    return make_jsonrpc_request('get_global_variable_value_by_name', variable_name)

@mcp.tool()
def get_global_variable_value_at_address(ea: Annotated[str, Field(description='Address of the global variable')]) -> str:
    """
    Read a global variable's value by its address (if known at compile-time)

    Prefer this function over the `data_read_*` functions.
    """
    return make_jsonrpc_request('get_global_variable_value_at_address', ea)

@mcp.tool()
def rename_function(function_address: Annotated[str, Field(description='Address of the function to rename')], new_name: Annotated[str, Field(description='New name for the function (empty for a default name)')]):
    """Rename a function"""
    return make_jsonrpc_request('rename_function', function_address, new_name)

@mcp.tool()
def set_function_prototype(function_address: Annotated[str, Field(description='Address of the function')], prototype: Annotated[str, Field(description='New function prototype')]):
    """Set a function's prototype"""
    return make_jsonrpc_request('set_function_prototype', function_address, prototype)

@mcp.tool()
def declare_c_type(c_declaration: Annotated[str, Field(description='C declaration of the type. Examples include: typedef int foo_t; struct bar { int a; bool b; };')]):
    """Create or update a local type from a C declaration"""
    return make_jsonrpc_request('declare_c_type', c_declaration)

@mcp.tool()
def set_local_variable_type(function_address: Annotated[str, Field(description='Address of the decompiled function containing the variable')], variable_name: Annotated[str, Field(description='Name of the variable')], new_type: Annotated[str, Field(description='New type for the variable')]):
    """Set a local variable's type"""
    return make_jsonrpc_request('set_local_variable_type', function_address, variable_name, new_type)

@mcp.tool()
def get_stack_frame_variables(function_address: Annotated[str, Field(description='Address of the disassembled function to retrieve the stack frame variables')]) -> list[StackFrameVariable]:
    """ Retrieve the stack frame variables for a given function """
    return make_jsonrpc_request('get_stack_frame_variables', function_address)

@mcp.tool()
def get_defined_structures() -> list[StructureDefinition]:
    """ Returns a list of all defined structures """
    return make_jsonrpc_request('get_defined_structures')

@mcp.tool()
def rename_stack_frame_variable(function_address: Annotated[str, Field(description='Address of the disassembled function to set the stack frame variables')], old_name: Annotated[str, Field(description='Current name of the variable')], new_name: Annotated[str, Field(description='New name for the variable (empty for a default name)')]):
    """ Change the name of a stack variable for an IDA function """
    return make_jsonrpc_request('rename_stack_frame_variable', function_address, old_name, new_name)

@mcp.tool()
def create_stack_frame_variable(function_address: Annotated[str, Field(description='Address of the disassembled function to set the stack frame variables')], offset: Annotated[str, Field(description='Offset of the stack frame variable')], variable_name: Annotated[str, Field(description='Name of the stack variable')], type_name: Annotated[str, Field(description='Type of the stack variable')]):
    """ For a given function, create a stack variable at an offset and with a specific type """
    return make_jsonrpc_request('create_stack_frame_variable', function_address, offset, variable_name, type_name)

@mcp.tool()
def set_stack_frame_variable_type(function_address: Annotated[str, Field(description='Address of the disassembled function to set the stack frame variables')], variable_name: Annotated[str, Field(description='Name of the stack variable')], type_name: Annotated[str, Field(description='Type of the stack variable')]):
    """ For a given disassembled function, set the type of a stack variable """
    return make_jsonrpc_request('set_stack_frame_variable_type', function_address, variable_name, type_name)

@mcp.tool()
def delete_stack_frame_variable(function_address: Annotated[str, Field(description='Address of the function to set the stack frame variables')], variable_name: Annotated[str, Field(description='Name of the stack variable')]):
    """ Delete the named stack variable for a given function """
    return make_jsonrpc_request('delete_stack_frame_variable', function_address, variable_name)

@mcp.tool()
def read_memory_bytes(memory_address: Annotated[str, Field(description='Address of the memory value to be read')], size: Annotated[int, Field(description='size of memory to read')]) -> str:
    """
    Read bytes at a given address.

    Only use this function if `get_global_variable_at` and `get_global_variable_by_name`
    both failed.
    """
    return make_jsonrpc_request('read_memory_bytes', memory_address, size)

@mcp.tool()
def data_read_byte(address: Annotated[str, Field(description='Address to get 1 byte value from')]) -> int:
    """
    Read the 1 byte value at the specified address.

    Only use this function if `get_global_variable_at` failed.
    """
    return make_jsonrpc_request('data_read_byte', address)

@mcp.tool()
def data_read_word(address: Annotated[str, Field(description='Address to get 2 bytes value from')]) -> int:
    """
    Read the 2 byte value at the specified address as a WORD.

    Only use this function if `get_global_variable_at` failed.
    """
    return make_jsonrpc_request('data_read_word', address)

@mcp.tool()
def data_read_dword(address: Annotated[str, Field(description='Address to get 4 bytes value from')]) -> int:
    """
    Read the 4 byte value at the specified address as a DWORD.

    Only use this function if `get_global_variable_at` failed.
    """
    return make_jsonrpc_request('data_read_dword', address)

@mcp.tool()
def data_read_qword(address: Annotated[str, Field(description='Address to get 8 bytes value from')]) -> int:
    """
    Read the 8 byte value at the specified address as a QWORD.

    Only use this function if `get_global_variable_at` failed.
    """
    return make_jsonrpc_request('data_read_qword', address)

@mcp.tool()
def data_read_string(address: Annotated[str, Field(description='Address to get string from')]) -> str:
    """
    Read the string at the specified address.

    Only use this function if `get_global_variable_at` failed.
    """
    return make_jsonrpc_request('data_read_string', address)

@mcp.tool()
def dbg_get_registers() -> list[dict[str, str]]:
    """Get all registers and their values. This function is only available when debugging."""
    return make_jsonrpc_request('dbg_get_registers')

@mcp.tool()
def dbg_get_call_stack() -> list[dict[str, str]]:
    """Get the current call stack."""
    return make_jsonrpc_request('dbg_get_call_stack')

@mcp.tool()
def dbg_list_breakpoints():
    """List all breakpoints in the program."""
    return make_jsonrpc_request('dbg_list_breakpoints')

@mcp.tool()
def dbg_start_process() -> str:
    """Start the debugger"""
    return make_jsonrpc_request('dbg_start_process')

@mcp.tool()
def dbg_exit_process() -> str:
    """Exit the debugger"""
    return make_jsonrpc_request('dbg_exit_process')

@mcp.tool()
def dbg_continue_process() -> str:
    """Continue the debugger"""
    return make_jsonrpc_request('dbg_continue_process')

@mcp.tool()
def dbg_run_to(address: Annotated[str, Field(description='Run the debugger to the specified address')]) -> str:
    """Run the debugger to the specified address"""
    return make_jsonrpc_request('dbg_run_to', address)

@mcp.tool()
def dbg_set_breakpoint(address: Annotated[str, Field(description='Set a breakpoint at the specified address')]) -> str:
    """Set a breakpoint at the specified address"""
    return make_jsonrpc_request('dbg_set_breakpoint', address)

@mcp.tool()
def dbg_delete_breakpoint(address: Annotated[str, Field(description='del a breakpoint at the specified address')]) -> str:
    """del a breakpoint at the specified address"""
    return make_jsonrpc_request('dbg_delete_breakpoint', address)

@mcp.tool()
def dbg_enable_breakpoint(address: Annotated[str, Field(description='Enable or disable a breakpoint at the specified address')], enable: Annotated[bool, Field(description='Enable or disable a breakpoint')]) -> str:
    """Enable or disable a breakpoint at the specified address"""
    return make_jsonrpc_request('dbg_enable_breakpoint', address, enable)

@mcp.tool()
def patch_bytes(address: Annotated[str, Field(description='Address to patch bytes at')], hex_bytes: Annotated[str, Field(description="Hexadecimal bytes to patch (e.g., '90 90 90' for three NOPs)")]) -> str:
    """Patch bytes at a specific address in the IDA database"""
    return make_jsonrpc_request('patch_bytes', address, hex_bytes)

@mcp.tool()
def create_function(address: Annotated[str, Field(description='Address to create function at')]) -> str:
    """Create a new function at the specified address"""
    return make_jsonrpc_request('create_function', address)

@mcp.tool()
def delete_function(address: Annotated[str, Field(description='Address of function to delete')]) -> str:
    """Delete a function at the specified address"""
    return make_jsonrpc_request('delete_function', address)

@mcp.tool()
def set_instruction_operand_type(address: Annotated[str, Field(description='Address of the instruction')], operand_index: Annotated[int, Field(description='Index of the operand (0-based)')], operand_type: Annotated[str, Field(description='Type of operand (offset, number, char, etc.)')]) -> str:
    """Set the operand type for an instruction"""
    return make_jsonrpc_request('set_instruction_operand_type', address, operand_index, operand_type)

@mcp.tool()
def create_struct(struct_name: Annotated[str, Field(description='Name of the structure to create')], members: Annotated[str, Field(description='Structure members in C format')]) -> str:
    """Create a new structure definition"""
    return make_jsonrpc_request('create_struct', struct_name, members)

@mcp.tool()
def add_struct_member(struct_name: Annotated[str, Field(description='Name of the existing structure')], member_name: Annotated[str, Field(description='Name of the new member')], member_type: Annotated[str, Field(description='Type of the new member')], offset: Annotated[int, Field(description='Offset of the member in bytes')]) -> str:
    """Add a member to an existing structure"""
    return make_jsonrpc_request('add_struct_member', struct_name, member_name, member_type, offset)

@mcp.tool()
def create_enum(enum_name: Annotated[str, Field(description='Name of the enumeration to create')], members: Annotated[str, Field(description="Enum members in format 'NAME1=value1,NAME2=value2'")]) -> str:
    """Create a new enumeration"""
    return make_jsonrpc_request('create_enum', enum_name, members)

@mcp.tool()
def set_data_type(address: Annotated[str, Field(description='Address to set data type at')], data_type: Annotated[str, Field(description='Data type to set')], size: Annotated[int, Field(description='Size of the data in bytes')]) -> str:
    """Set the data type at a specific address"""
    return make_jsonrpc_request('set_data_type', address, data_type, size)

@mcp.tool()
def create_array(address: Annotated[str, Field(description='Address to create array at')], element_type: Annotated[str, Field(description='Type of array elements')], count: Annotated[int, Field(description='Number of elements in the array')]) -> str:
    """Create an array at the specified address"""
    return make_jsonrpc_request('create_array', address, element_type, count)

@mcp.tool()
def add_cross_reference(from_address: Annotated[str, Field(description='Source address of the cross reference')], to_address: Annotated[str, Field(description='Target address of the cross reference')], ref_type: Annotated[str, Field(description='Type of reference (code, data)')]) -> str:
    """Add a cross reference between two addresses"""
    return make_jsonrpc_request('add_cross_reference', from_address, to_address, ref_type)

@mcp.tool()
def delete_cross_reference(from_address: Annotated[str, Field(description='Source address of the cross reference')], to_address: Annotated[str, Field(description='Target address of the cross reference')]) -> str:
    """Delete a cross reference between two addresses"""
    return make_jsonrpc_request('delete_cross_reference', from_address, to_address)

