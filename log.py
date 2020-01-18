from opencensus.ext.azure.trace_exporter import AzureExporter
from opencensus.trace.samplers import ProbabilitySampler
from opencensus.trace.tracer import Tracer

# TODO: replace the all-zero GUID with your instrumentation key.
tracer = Tracer(
    exporter=AzureExporter(
        connection_string='InstrumentationKey=ba4cf7af-e196-4725-82b3-a430b734d0be'),
    sampler=ProbabilitySampler(1.0),
)

def valuePrompt():
    with tracer.span(name="test") as span:
        line = input("Enter a value: ")
        print(line)

def main():
    while True:
        valuePrompt()

if __name__ == "__main__":
    main()