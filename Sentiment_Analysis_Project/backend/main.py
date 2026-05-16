"""
FastAPI Backend for Sentiment Analysis
NeuralAICodeCraft - Complete NLP Project
"""

from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
import uvicorn
from typing import List
import time

from models import (
    SentimentRequest, SentimentResponse, 
    BatchRequest, BatchResponse, 
    HealthResponse, ModelInfoResponse
)
from sentiment_analyzer import analyzer

# Create FastAPI app
app = FastAPI(
    title="Sentiment Analysis API",
    description="API for sentiment analysis using Logistic Regression and Naive Bayes",
    version="1.0.0",
    docs_url="/docs",
    redoc_url="/redoc"
)

# Add CORS middleware (for frontend access)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # In production, replace with specific origins
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ============================================
# HEALTH CHECK ENDPOINTS
# ============================================

@app.get("/", response_model=HealthResponse)
async def root():
    """Root endpoint - API health check"""
    return HealthResponse(
        status="healthy",
        models_loaded=True,
        available_models=["logistic", "naivebayes", "both"]
    )

@app.get("/health", response_model=HealthResponse)
async def health_check():
    """Health check endpoint"""
    return HealthResponse(
        status="healthy",
        models_loaded=True,
        available_models=["logistic", "naivebayes", "both"]
    )

# ============================================
# MODEL INFO ENDPOINTS
# ============================================

@app.get("/model-info", response_model=ModelInfoResponse)
async def get_model_info():
    """Get information about loaded models"""
    try:
        info = analyzer.get_model_info()
        return ModelInfoResponse(**info)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# ============================================
# SENTIMENT ANALYSIS ENDPOINTS
# ============================================

@app.post("/predict", response_model=List[SentimentResponse])
async def predict_sentiment(request: SentimentRequest):
    """
    Predict sentiment of a single text
    """
    try:
        results = []
        
        if request.model == 'logistic':
            result = analyzer.predict_logistic(request.text)
            results.append(SentimentResponse(
                text=request.text,
                sentiment=result['sentiment'],
                confidence=result['confidence'],
                probabilities=result['probabilities'],
                model=result['model']
            ))
        
        elif request.model == 'naivebayes':
            result = analyzer.predict_naivebayes(request.text)
            results.append(SentimentResponse(
                text=request.text,
                sentiment=result['sentiment'],
                confidence=result['confidence'],
                probabilities=result['probabilities'],
                model=result['model']
            ))
        
        elif request.model == 'both':
            logistic_result = analyzer.predict_logistic(request.text)
            naivebayes_result = analyzer.predict_naivebayes(request.text)
            
            results.append(SentimentResponse(
                text=request.text,
                sentiment=logistic_result['sentiment'],
                confidence=logistic_result['confidence'],
                probabilities=logistic_result['probabilities'],
                model=logistic_result['model']
            ))
            
            results.append(SentimentResponse(
                text=request.text,
                sentiment=naivebayes_result['sentiment'],
                confidence=naivebayes_result['confidence'],
                probabilities=naivebayes_result['probabilities'],
                model=naivebayes_result['model']
            ))
        
        else:
            raise HTTPException(status_code=400, detail="Invalid model specified")
        
        return results
        
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/predict-batch", response_model=BatchResponse)
async def predict_batch(request: BatchRequest):
    """
    Predict sentiment for multiple texts
    """
    try:
        start_time = time.time()
        
        results = analyzer.predict_batch(request.texts, request.model)
        
        processing_time = time.time() - start_time
        
        return BatchResponse(
            results=results,
            total_analyzed=len(results),
            model_used=request.model
        )
        
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# ============================================
# UTILITY ENDPOINTS
# ============================================

@app.post("/analyze-detailed")
async def analyze_detailed(request: SentimentRequest):
    """
    Get detailed analysis including word importance
    """
    try:
        result = analyzer.predict_both(request.text)
        
        # Extract important words (simplified)
        words = request.text.split()
        
        return JSONResponse({
            'text': request.text,
            'logistic': result['logistic'],
            'naivebayes': result['naivebayes'],
            'agreement': result['logistic']['sentiment'] == result['naivebayes']['sentiment'],
            'text_length': len(request.text),
            'word_count': len(words),
            'unique_words': len(set(words))
        })
        
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# ============================================
# RUN THE APP
# ============================================

if __name__ == "__main__":
    uvicorn.run(
        "main:app",
        host="0.0.0.0",
        port=8000,
        reload=True,
        log_level="info"
    )