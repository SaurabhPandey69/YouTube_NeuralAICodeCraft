"""
NLP VISUAL DEMO with Matplotlib
NeuralAICodeCraft - Visualizing NLP Concepts
"""

import matplotlib.pyplot as plt
import matplotlib.patches as patches
from matplotlib.patches import FancyBboxPatch, Circle
import numpy as np

def create_nlp_phases_diagram():
    """Create a visual diagram of NLP phases"""
    fig, ax = plt.subplots(1, 1, figsize=(12, 4))
    
    phases = [
        "Morphological\n(Word Structure)",
        "Syntactic\n(Grammar)",
        "Semantic\n(Meaning)",
        "Discourse\n(Context)",
        "Pragmatic\n(Intent)"
    ]
    
    colors = ['#8B5CF6', '#06B6D4', '#D9F99D', '#F59E0B', '#EF4444']
    
    for i, (phase, color) in enumerate(zip(phases, colors)):
        box = FancyBboxPatch(
            (i*2, 0.5), 1.5, 1.5,
            boxstyle="round,pad=0.1",
            facecolor=color,
            edgecolor='white',
            linewidth=2,
            alpha=0.8
        )
        ax.add_patch(box)
        ax.text(i*2 + 0.75, 1.25, phase, ha='center', va='center', 
                fontsize=10, fontweight='bold', color='white')
        
        if i < 4:
            ax.annotate('→', xy=(i*2 + 1.7, 1.25), xytext=(i*2 + 1.5, 1.25),
                       fontsize=20, color='white')
    
    ax.set_xlim(-0.5, 11)
    ax.set_ylim(0, 3)
    ax.axis('off')
    ax.set_title('Five Phases of Natural Language Processing', fontsize=14, 
                 fontweight='bold', color='#8B5CF6', pad=20)
    
    plt.tight_layout()
    plt.savefig('nlp_phases_diagram.png', dpi=150, bbox_inches='tight', 
                facecolor='#0A0A0F')
    plt.show()
    print("✅ Saved: nlp_phases_diagram.png")

def create_tokenization_visual():
    """Visualize tokenization process"""
    fig, ax = plt.subplots(1, 1, figsize=(12, 3))
    
    text = "I ❤️ Natural Language Processing"
    tokens = ["I", "❤️", "Natural", "Language", "Processing"]
    
    # Background
    ax.set_facecolor('#0A0A0F')
    
    # Original text box
    orig_box = FancyBboxPatch((0.5, 1.5), 8, 0.8, 
                               boxstyle="round,pad=0.1",
                               facecolor='#8B5CF6', alpha=0.3,
                               edgecolor='#8B5CF6', linewidth=2)
    ax.add_patch(orig_box)
    ax.text(4.5, 1.9, f'Original Text: "{text}"', ha='center', va='center',
            fontsize=12, color='white')
    
    # Arrow
    ax.annotate('↓ TOKENIZE ↓', xy=(4.5, 1.4), xytext=(4.5, 1.4),
               fontsize=10, color='#D9F99D', ha='center')
    
    # Tokens
    token_boxes = []
    for i, token in enumerate(tokens):
        box = FancyBboxPatch((0.5 + i*1.8, 0.2), 1.5, 0.6,
                             boxstyle="round,pad=0.05",
                             facecolor='#06B6D4', alpha=0.7,
                             edgecolor='white', linewidth=1)
        ax.add_patch(box)
        ax.text(0.5 + i*1.8 + 0.75, 0.5, token, ha='center', va='center',
                fontsize=10, color='white', fontweight='bold')
    
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 3)
    ax.axis('off')
    ax.set_title('Tokenization: Breaking Text into Tokens', fontsize=12,
                 fontweight='bold', color='#06B6D4', pad=20)
    
    plt.tight_layout()
    plt.savefig('tokenization_visual.png', dpi=150, bbox_inches='tight',
                facecolor='#0A0A0F')
    plt.show()
    print("✅ Saved: tokenization_visual.png")

def create_stemming_lemmatization_visual():
    """Compare stemming and lemmatization"""
    fig, axes = plt.subplots(1, 2, figsize=(12, 5))
    
    words = ["running", "better", "studies", "went", "happiness"]
    porter_stems = ["run", "better", "studi", "went", "happi"]
    snowball_stems = ["run", "better", "studi", "went", "happi"]
    lemmas = ["run", "good", "study", "go", "happiness"]
    
    # Stemming plot
    ax1 = axes[0]
    ax1.set_facecolor('#0A0A0F')
    y_pos = np.arange(len(words))
    ax1.barh(y_pos, [1]*len(words), color='#8B5CF6', alpha=0.3)
    
    for i, (word, stem) in enumerate(zip(words, porter_stems)):
        ax1.text(0.1, i, f"{word} → {stem}", fontsize=10, 
                va='center', color='white')
    
    ax1.set_yticks([])
    ax1.set_xlim(0, 1)
    ax1.set_title('Stemming (Porter)', fontsize=12, fontweight='bold',
                  color='#8B5CF6')
    ax1.axis('off')
    
    # Lemmatization plot
    ax2 = axes[1]
    ax2.set_facecolor('#0A0A0F')
    
    for i, (word, lemma) in enumerate(zip(words, lemmas)):
        ax2.text(0.1, i, f"{word} → {lemma}", fontsize=10,
                va='center', color='white')
    
    ax2.set_yticks([])
    ax2.set_xlim(0, 1)
    ax2.set_title('Lemmatization (WordNet)', fontsize=12, fontweight='bold',
                  color='#06B6D4')
    ax2.axis('off')
    
    plt.suptitle('Stemming vs Lemmatization', fontsize=14, fontweight='bold',
                 color='#D9F99D')
    plt.tight_layout()
    plt.savefig('stemming_vs_lemmatization.png', dpi=150, bbox_inches='tight',
                facecolor='#0A0A0F')
    plt.show()
    print("✅ Saved: stemming_vs_lemmatization.png")

def create_ner_visual():
    """Visualize Named Entity Recognition"""
    fig, ax = plt.subplots(1, 1, figsize=(12, 4))
    
    text = "Elon Musk founded SpaceX in Hawthorne, California on March 14, 2002"
    entities = [
        ("Elon Musk", "PERSON", '#22C55E'),
        ("SpaceX", "ORGANIZATION", '#8B5CF6'),
        ("Hawthorne", "LOCATION", '#F59E0B'),
        ("California", "LOCATION", '#F59E0B'),
        ("March 14, 2002", "DATE", '#06B6D4')
    ]
    
    ax.set_facecolor('#0A0A0F')
    
    # Background box for text
    text_box = FancyBboxPatch((0.5, 2), 11, 0.8,
                              boxstyle="round,pad=0.1",
                              facecolor='#1A1A2E',
                              edgecolor='#8B5CF6',
                              linewidth=1)
    ax.add_patch(text_box)
    
    # Highlight entities in text
    current_x = 0.7
    remaining_text = text
    for entity, label, color in entities:
        if entity in remaining_text:
            parts = remaining_text.split(entity, 1)
            # Text before entity
            if parts[0]:
                ax.text(current_x, 2.4, parts[0], ha='left', va='center',
                       fontsize=10, color='white')
                current_x += len(parts[0]) * 0.1
            
            # Entity with highlight
            entity_box = FancyBboxPatch((current_x, 2.15), len(entity)*0.1, 0.5,
                                       boxstyle="round,pad=0.02",
                                       facecolor=color, alpha=0.3,
                                       edgecolor=color, linewidth=1)
            ax.add_patch(entity_box)
            ax.text(current_x + len(entity)*0.05, 2.4, entity,
                   ha='center', va='center', fontsize=10,
                   color='white', fontweight='bold')
            current_x += len(entity) * 0.1
            
            # Label below entity
            ax.text(current_x - len(entity)*0.05, 1.9, label,
                   ha='center', va='center', fontsize=8,
                   color=color, fontweight='bold')
            
            remaining_text = parts[1]
    
    # Remaining text
    if remaining_text:
        ax.text(current_x, 2.4, remaining_text, ha='left', va='center',
               fontsize=10, color='white')
    
    ax.set_xlim(0, 12)
    ax.set_ylim(1.5, 3.5)
    ax.axis('off')
    ax.set_title('Named Entity Recognition (NER) - Extracting Entities from Text',
                fontsize=12, fontweight='bold', color='#D9F99D', pad=20)
    
    plt.tight_layout()
    plt.savefig('ner_visual.png', dpi=150, bbox_inches='tight',
                facecolor='#0A0A0F')
    plt.show()
    print("✅ Saved: ner_visual.png")

# Generate all visualizations
if __name__ == "__main__":
    print("🎨 Generating NLP Visualizations...")
    print("-" * 50)
    
    create_nlp_phases_diagram()
    create_tokenization_visual()
    create_stemming_lemmatization_visual()
    create_ner_visual()
    
    print("\n✅ All visualizations saved!")

    