import json
import os
import sys
import pandas as pd
from reportcompiler.plugins.source_parsers.python \
    import PythonParser
from reportcompiler.plugins.source_parsers.base \
    import SourceParser


def generate_failed_contexts(report_path):
    try:
        with open(os.path.join(report_path,
                               '_meta',
                               'last_debug_errors'), 'r') as f:
            last_values = json.load(f)
    except FileNotFoundError:
        raise FileNotFoundError(
            'There is no file with debugging data, please retry '
            'generating a document on debug mode')

    for frag in last_values:
        print("Error on fragment '{}' ({})".format(
            frag['metadata']['fragment_name'],
            frag['timestamp']))
        doc_var = frag['doc_var']
        data = {name: pd.DataFrame(data)
                for name, data in frag['data'].items()}
        metadata = frag['metadata']

        fragment = os.path.basename(metadata['fragment_path'])
        _, ext = os.path.splitext(fragment)

        generator_info = metadata.get('context_generator')
        if isinstance(generator_info, str):
            generator = SourceParser.get(id=generator_info,
                                         extension=ext)
        elif isinstance(generator_info, dict):
            generator = SourceParser.get(
                            id=generator_info[ext])

        if generator.__class__ == PythonParser:
            sys.path.append(os.path.join(report_path, frag['report'], 'src'))
            try:
                ctx = PythonParser().generate_context(doc_var,
                                                      data,
                                                      metadata)
                print('\n{}\n'.format(ctx))
                print('*** {} has finished successfully.'.format(fragment))
            except Exception:
                print('*** {} has finished with errors.'.format(fragment))
        else:
            print("*** {} doesn't use python, skipping...".format(fragment))


if __name__ == '__main__':
    generate_failed_contexts(report_path=os.environ['REPORTS_PATH'])
