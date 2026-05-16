"""
Pydantic Models for FastAPI
NeuralAICodeCraft - Request/Response schemas
"""

from pydantic import BaseModel, Field
from typing import List, Dict, Optional

class SentimentRequest(BaseModel):
    """Request model for sentiment analysis"""
    text: str = Field(..., min_length=1, max_length=1000, description="Text to analyze")
    model: Optional[str] = Field('both', description="Model to use: 'logistic', 'naivebayes', or 'both'")

class SentimentResponse(BaseModel):
    """Response model for sentiment analysis"""
    text: str
    sentiment: str
    confidence: float
    probabilities: Dict[str, float]
    model: str

class BatchRequest(BaseModel):
    """Request model for batch analysis"""
    texts: List[str] = Field(..., min_items=1, max_items=100)
    model: Optional[str] = Field('logistic')

class BatchResponse(BaseModel):
    """Response model for batch analysis"""
    results: List[Dict]
    total_analyzed: int
    model_used: str

class HealthResponse(BaseModel):
    """Health check response"""
    status: str
    models_loaded: bool
    available_models: List[str]

class ModelInfoResponse(BaseModel):
    """Model information response"""
    logistic_regression: Dict
    naive_bayes: Dict
    features: List[str]